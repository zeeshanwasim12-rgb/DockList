import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = Path(os.environ.get("TODO_DB_PATH", str(Path(__file__).parent / "data" / "tasks.db")))


@contextmanager
def connect_db():
    """Open the SQLite database stored on the mounted persistent volume."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def initialize_db():
    """Create the task table and seed examples only on the first run."""
    with connect_db() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL CHECK(length(title) <= 200),
            completed INTEGER NOT NULL DEFAULT 0
        )""")
        if db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 0:
            db.executemany("INSERT INTO tasks (title, completed) VALUES (?, ?)", [
                ("Read Unit 1 & Unit 2 Docker notes", 1),
                ("Build the Dockerized To-Do app", 0),
                ("Practice docker build and docker run", 0),
            ])


def serialize_task(row):
    return {"id": row["id"], "title": row["title"], "completed": bool(row["completed"])}


initialize_db()
@app.route("/")
def index():
    """Serve the main HTML page (the To-Do user interface)."""
    return render_template("index.html")


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    """
    Return ALL tasks as JSON.

    The browser (static/script.js) fetches this list and then decides
    which tasks to show (All / Active / Completed) on the client side.
    """
    with connect_db() as db:
        rows = db.execute("SELECT id, title, completed FROM tasks ORDER BY id").fetchall()
    return jsonify([serialize_task(row) for row in rows])


@app.route("/add", methods=["POST"])
def add_task():
    """
    Add a new task.

    Expects JSON in the request body: {"title": "Some task"}
    Returns the newly created task as JSON with HTTP status 201 (Created).
    """
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()

    if not title:
        return jsonify({"error": "Task title cannot be empty."}), 400
    if len(title) > 200:
        return jsonify({"error": "Task title is too long (max 200 characters)."}), 400

    with connect_db() as db:
        cursor = db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        row = db.execute("SELECT id, title, completed FROM tasks WHERE id = ?", (cursor.lastrowid,)).fetchone()
    return jsonify(serialize_task(row)), 201


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    """
    Toggle a task between completed and not-completed.

    <int:task_id> tells Flask to read the id from the URL as an integer,
    e.g. POST /complete/2 toggles the task whose id is 2.
    """
    with connect_db() as db:
        db.execute("UPDATE tasks SET completed = 1 - completed WHERE id = ?", (task_id,))
        row = db.execute("SELECT id, title, completed FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if row is None:
        return jsonify({"error": "Task not found."}), 404
    return jsonify(serialize_task(row))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Delete a task by its id."""
    with connect_db() as db:
        cursor = db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        return jsonify({"error": "Task not found."}), 404
    return jsonify({"message": "Task deleted."})


@app.route("/health")
def health():
    """Monitoring/readiness endpoint; also verifies the database is reachable."""
    try:
        with connect_db() as db:
            db.execute("SELECT 1")
        return jsonify({"status": "healthy", "storage": "available"})
    except sqlite3.Error:
        app.logger.exception("Health check could not reach the database")
        return jsonify({"status": "unhealthy", "storage": "unavailable"}), 503

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=False)

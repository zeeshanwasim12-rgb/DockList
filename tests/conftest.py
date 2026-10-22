import pytest

import app as todo_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(todo_app, "DB_PATH", tmp_path / "tasks.db")
    todo_app.initialize_db()
    with todo_app.connect_db() as db:
        db.execute("DELETE FROM tasks")
        db.execute("DELETE FROM sqlite_sequence WHERE name = 'tasks'")
    todo_app.initialize_db()
    todo_app.app.config.update(TESTING=True)
    with todo_app.app.test_client() as test_client:
        yield test_client
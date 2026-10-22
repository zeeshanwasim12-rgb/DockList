def test_home_and_frontend_assets_load(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Docklist" in response.data
    assert client.get("/static/style.css").status_code == 200
    assert client.get("/static/script.js").status_code == 200


def test_seed_tasks_are_returned_as_json(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    tasks = response.get_json()
    assert [task["title"] for task in tasks] == [
        "Read Unit 1 & Unit 2 Docker notes",
        "Build the Dockerized To-Do app",
        "Practice docker build and docker run",
    ]
    assert tasks[0]["completed"] is True
    assert tasks[1]["completed"] is False


def test_create_validate_complete_and_delete_task(client):
    created = client.post("/add", json={"title": "  Write tests  "})
    assert created.status_code == 201
    task = created.get_json()
    assert task["title"] == "Write tests"
    assert task["completed"] is False

    completed = client.post(f"/complete/{task['id']}")
    assert completed.status_code == 200
    assert completed.get_json()["completed"] is True

    deleted = client.post(f"/delete/{task['id']}")
    assert deleted.status_code == 200
    assert all(item["id"] != task["id"] for item in client.get("/api/tasks").get_json())


def test_invalid_task_titles_and_missing_ids(client):
    assert client.post("/add", json={"title": "  "}).status_code == 400
    assert client.post("/add", json={"title": "x" * 201}).status_code == 400
    assert client.post("/complete/999").status_code == 404
    assert client.post("/delete/999").status_code == 404


def test_health_endpoint_checks_storage(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy", "storage": "available"}
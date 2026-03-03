from fastapi.testclient import TestClient

from fastapi_todo_list.app import app

client = TestClient(app)

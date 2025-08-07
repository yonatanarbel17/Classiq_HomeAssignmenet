import sys
import os
import time
import pytest
from fastapi.testclient import TestClient

# Make app importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.main import app

client = TestClient(app)

VALID_QASM3 = """
OPENQASM 3.0;
include "stdgates.inc";
qubit q[2];
bit c[2];
h q[0];
cx q[0], q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
"""

@pytest.fixture(scope="module")
def task_id():
    response = client.post("/tasks", json={"qc": VALID_QASM3})
    assert response.status_code == 202
    return response.json()["task_id"]

def test_submit_task(task_id):
    assert isinstance(task_id, str)

def test_get_task_result(task_id):
    max_retries = 10
    for _ in range(max_retries):
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        status = data.get("status")

        if status == "completed":
            result = data.get("result")
            print("DEBUG result:", result)  # Optional for inspection
            assert isinstance(result, dict)
            assert all(isinstance(k, str) and isinstance(v, int) for k, v in result.items())
            return

        if status == "error":
            pytest.fail("Task failed during execution.")

        time.sleep(1)

    pytest.fail("Task did not complete in time.")

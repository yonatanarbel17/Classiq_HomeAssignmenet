from fastapi import FastAPI, HTTPException
from rq import Queue
from redis import Redis
from uuid import uuid4
from typing import Dict, Any

# Connect to Redis. The hostname 'redis' is the service name defined in docker-compose.
redis_conn = Redis(host='redis', port=6379)
q = Queue(connection=redis_conn)

app = FastAPI()

# Import the worker function that will be executed in the background.
from .worker import execute_quantum_circuit

@app.post("/tasks", status_code=202)
async def create_task(payload: Dict[str, str]):
    """
    This endpoint receives a quantum circuit payload and initiates its asynchronous processing.
    """
    qasm3_string = payload.get("qc")
    if not qasm3_string:
        raise HTTPException(status_code=400, detail={"message": "Invalid input. 'qc' field is required."})

    task_id = str(uuid4())

    # Enqueue the job to be processed by the worker.
    job = q.enqueue(execute_quantum_circuit, qasm3_string, job_id=task_id)

    return {"task_id": job.id, "message": "Task submitted successfully."}

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    """
    This endpoint retrieves the results of a previously submitted quantum circuit using its unique task identifier.
    """
    job = q.fetch_job(task_id)

    if job is None:
        raise HTTPException(status_code=404, detail={"status": "error", "message": "Task not found."})

    status = job.get_status()

    if status == 'finished':
        result = job.return_value 
        return {"status": "completed", "result": result}
    elif status in ('queued', 'started'):
        return {"status": "pending", "message": "Task is still in progress."}
    else:
        return {"status": "error", "message": "An error occurred during task processing."}

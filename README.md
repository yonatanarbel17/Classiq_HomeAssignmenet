# Quantum Circuit API

This project implements a system architecture that supports a detailed API for executing quantum circuits. The system is designed to handle asynchronous processing, ensure task integrity, and is deployed using Docker Compose for containerization and orchestration.

---

## Getting Started

To set up and run this project, you need to have **Docker Desktop** installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yonatanarbel17/Classiq_HomeAssignmenet.git
   cd Classiq_HomeAssignmenet
   ```

2. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```

   This will start the following services:
   - FastAPI server (`api_server`)
   - Redis message broker (`redis`)
   - Background worker (`worker`)

3. **Run tests:**
   ```bash
   docker-compose build test_runner
   docker-compose run test_runner
   ```

---

## Architecture Overview

The system consists of three core components:

### API Server (`api_server`)
- Built with FastAPI  
- Exposes endpoints to submit quantum circuits and query results  
- Enqueues tasks in Redis using RQ

### Worker (`worker`)
- Runs in a separate container  
- Listens for jobs from Redis  
- Executes quantum circuits using Qiskit's AerSimulator  
- Stores the results back in Redis

### Redis (`redis`)
- Acts as a message broker and storage layer  
- Queues submitted tasks and holds their result status

This architecture provides fault tolerance and scalability: tasks aren't lost if the worker crashes, and components can be scaled independently.

---

## Features

- Full containerized architecture using Docker Compose
- FastAPI web service to submit and monitor quantum circuits
- Background worker with Qiskit simulation
- Redis-based queuing and result tracking
- Integration tests using `pytest`, `httpx`, and `pytest-asyncio`

---

## API Endpoints

### POST `/tasks`
Submit a new quantum circuit for execution.

**Request Body:**
```json
{
  "qc": "OPENQASM 3.0; ... "
}
```

**Response:**
```json
{
  "task_id": "1234-abcd",
  "message": "Task submitted successfully."
}
```

---

### GET `/tasks/{task_id}`
Retrieve the status or result of a submitted task.

**Response (in progress):**
```json
{
  "status": "pending",
  "message": "Task is still in progress."
}
```

**Response (completed):**
```json
{
  "status": "completed",
  "result": {
    "00": 512,
    "11": 512
  }
}
```

**Response (error):**
```json
{
  "status": "error",
  "message": "An error occurred during task processing."
}
```

---


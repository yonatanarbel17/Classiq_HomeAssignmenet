# Quantum Circuit API

This project implements a system architecture that supports a detailed API for executing quantum circuits. The system is designed to handle asynchronous processing, ensure task integrity, and is deployed using Docker Compose for containerization and orchestration.

***

### 🚀 Getting Started

To set up and run this project, you need to have **Docker Desktop** installed.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Build and run the containers:**
    ```bash
    docker-compose up --build
    ```
    This command will build the necessary Docker images and start three services: a Redis database, a FastAPI server, and a background worker.

***

### 🏗️ System Architecture

The system is built on a microservices architecture with three main components orchestrated by Docker Compose:

* **API Server (`api_server`)**: A web service built with FastAPI that exposes two HTTP endpoints. It receives quantum circuit payloads and enqueues them for processing. This service is lightweight and remains responsive to new requests.
* **Background Worker (`worker`)**: A separate process that listens to a Redis queue. It picks up tasks (quantum circuits), executes them using Qiskit's `AerSimulator`, and stores the results.
* **Message Broker (`redis`)**: A Redis instance that serves as both a message queue for distributing tasks to the worker and a data store for managing the state and results of each task.

This asynchronous architecture ensures that the system is robust. Submitted tasks are persisted in the Redis queue, so they won't be lost even if the worker service goes down. When the worker is restarted, it will continue processing tasks from the queue.

***

### 🔌 API Endpoints

The API supports the following endpoints:

#### `POST /tasks`
**Description**: This endpoint receives a quantum circuit payload and initiates its asynchronous processing. It then returns a task ID that can be used to track the processing status.
**Input**: A JSON payload with the key "qc" and a string value containing a serialized quantum circuit in QASM3 format.
**Example Input**:
```json
{
  "qc": "OPENQASM 3.0; ... "
}
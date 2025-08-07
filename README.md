# Quantum Circuit API

This project implements a containerized microservice architecture for executing quantum circuits asynchronously via a RESTful API. It uses FastAPI for the web server, Redis as a message broker and result store, and RQ for background task processing. Quantum circuits are executed using Qiskit's AerSimulator.

## Repository

https://github.com/yonatanarbel17/Classiq_HomeAssignmenet

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your system
- Python 3.9+ if you intend to run components locally outside Docker

### Clone the repository

```bash
git clone https://github.com/yonatanarbel17/Classiq_HomeAssignmenet.git
cd Classiq_HomeAssignmenet

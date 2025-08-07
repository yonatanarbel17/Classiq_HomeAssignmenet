from redis import Redis
from rq import Worker, Queue

# Connect to Redis (adjust host/port if needed for Docker Compose)
redis_conn = Redis(host='redis', port=6379)

# Create a worker for the 'default' queue using the connection
worker = Worker(queues=['default'], connection=redis_conn)
worker.work()

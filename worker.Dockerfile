# Use the same base image to ensure consistency
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the worker code and the entrypoint file
COPY ./app ./app
COPY worker_entrypoint.py .

# Command to run the RQ worker
CMD ["python", "worker_entrypoint.py"]
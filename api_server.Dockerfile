# Use an official Python runtime that is stable for FastAPI and its dependencies.
FROM python:3.11-slim-buster

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker's build cache.
COPY requirements.txt .

# Install the Python dependencies from the requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container.
COPY ./app ./app
COPY ./tests ./tests


# Expose the port that the FastAPI application will run on.
EXPOSE 8000

# Command to start the application using uvicorn.
# The 'app.main:app' syntax tells uvicorn to look for the 'app' object in the 'main' module inside the 'app' directory.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
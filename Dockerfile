# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 python3-opencv

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Command to run the application (replace with your application's entry point)
ENTRYPOINT ["python", "/app/v2m.py"]
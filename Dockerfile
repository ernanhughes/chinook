# Use an official Python runtime as a base image
FROM python:3.11-slim
# Set the working directory in docker
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY ./chinook /app
COPY ./.env_example /app/.env
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable for Uvicorn
ENV UVICORN_HOST=0.0.0.0 UVICORN_PORT=80
# Run fastapi app using uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


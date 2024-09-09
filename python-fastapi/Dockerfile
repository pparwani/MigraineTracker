# Pull the official base image
FROM python:3.12-slim

# Set the working directory in the Docker container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
# Using --no-cache-dir to keep the image size down
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Optional: Set environment variables for debugging
ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

# Command to run on container start
# Choose one of the following depending on your scenario:
# 1. Standard Uvicorn command (for production or general use)
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# 2. Uvicorn with reloading enabled (for development)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# 3. Debugging with debugpy (for debugging purposes)
# CMD ["python3", "-m", "debugpy", "--listen", "0.0.0.0:8199​⬤
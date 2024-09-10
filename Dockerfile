# Pull the official base image
FROM python:3.12-slim

# Set the working directory in the Docker container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD  ["python3", "-m","debugpy","--listen","0.0.0.0:8199","--wait-for-client","app/main.py"]
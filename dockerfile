# Base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Copy Pipfile files
COPY Pipfile Pipfile.lock ./

# Install Python dependencies
RUN pipenv install --deploy --system

# Copy project code
COPY . .

# Default command (optional)
CMD ["python", "main.py"]

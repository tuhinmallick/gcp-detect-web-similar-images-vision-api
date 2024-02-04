# Use Python 3.11-slim as base image
FROM python:3.11-slim

# Set unbuffered mode for Python stdout and stderr (helps with logging)
ENV PYTHONUNBUFFERED True

# Install Poetry at the latest stable version
RUN pip install --no-cache-dir poetry==1.6.1

# Disable Poetry's virtual environment as dependencies will be installed globally
RUN poetry config virtualenvs.create false

# Set the working directory
WORKDIR /demo

# Copy only dependencies files to cache them in docker layer
COPY pyproject.toml poetry.lock* ./

# Install project dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of your application
COPY . ./

# Expose the correct port
EXPOSE 80

# Switch to a non-root user for security
RUN useradd -m myuser
USER myuser

# Command to run your application
CMD ["python", "./ui.py"]

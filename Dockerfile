# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code to the container
COPY . .

# Expose the port on which your Django application runs
EXPOSE 8000

# Define the command to start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

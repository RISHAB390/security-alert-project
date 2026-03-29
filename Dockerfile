# Use Python as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your files into the container
COPY . .

# Run the detector script when the container starts
CMD ["python", "detector.py"]
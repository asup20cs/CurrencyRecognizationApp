# Base image with Python 3.12 (adjust if needed)
FROM python:slim-bookworm

# Create a working directory within the container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using pip (replace with your actual requirements)
RUN pip install -r requirements.txt


# Set the main script to execute
CMD ["python", "gui.py"]
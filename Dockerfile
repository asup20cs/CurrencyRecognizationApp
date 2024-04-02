# Base image with Python 3.8 (adjust if needed)
FROM python:3.12

# Create a working directory within the container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using pip (replace with your actual requirements)
RUN pip install -r requirements.txt


# Set the main script to execute
CMD ["python", "gui.py"]
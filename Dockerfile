# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found, skipping"

# Run main.py by default
CMD ["python", "main.py"]

# Use the official Python image as base image
FROM python:3.9-slim

# Set environment variables
ENV OPENAI_API_KEY="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"
ENV DEEPGRAM_API_KEY="61c5ee4557b33c33767d8cd6efcb981ec811352f"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5001 to the outside world
EXPOSE 5001

# Command to run the Flask application
CMD ["python", "app.py"]

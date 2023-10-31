FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Update package lists
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 gcc g++ git build-essential libpoppler-cpp-dev pkg-config poppler-utils tesseract-ocr libtesseract-dev -y

# Make working directories
RUN  mkdir -p  /app
WORKDIR  /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy every file in the source folder to the created working directory
COPY  ./.src .

# Start the application
CMD ["python", "app.py"]
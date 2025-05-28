# Use an official Python runtime as a parent image
FROM python:3.12.10-alpine

# Set the working directory in the container
WORKDIR /string_splitter

# Copy the current directory contents into the container at /app
COPY ./requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY .env .
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 5000

# Run the Uvicorn server when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
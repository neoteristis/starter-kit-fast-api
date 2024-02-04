FROM bitnami/python:3.10.11-debian-11-r11

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the app code to the container
COPY ./app /code/app

# Start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

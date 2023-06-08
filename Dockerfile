FROM python:3.8-slim
# Set the working directory
WORKDIR /opt
# Copy the requirements file and install dependencies
COPY requirements.txt /opt
RUN pip install -r requirements.txt
# Copy the application code
COPY ./ /opt
# Install cron
RUN apt-get update && apt-get install -y cron
CMD ["python3", "main.py"]
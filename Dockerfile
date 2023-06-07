FROM python:3.8-slim

# Set the working directory
WORKDIR /opt

# Copy the requirements file and install dependencies
COPY requirements.txt /opt
RUN pip install -r requirements.txt

# Copy the application code
COPY ./ /opt

# Install cron (if needed for your application)
RUN apt-get update && apt-get install -y cron


ENV ENVIRONMENT=local

# Fetch sensitive information only when running on AWS
RUN if [ "$ENVIRONMENT" = "aws" ]; then \
      apt-get install -y awscli && \
      export PARAM1=$(aws ssm get-parameter --name "telegram_api_key" --with-decryption --query "Parameter.Value" --output text) && \
      export PARAM2=$(aws ssm get-parameter --name "telegram_bot_name" --with-decryption --query "Parameter.Value" --output text) && \
      export PARAM3=$(aws ssm get-parameter --name "openai_key" --with-decryption --query "Parameter.Value" --output text) \
    ; fi


CMD ["python3", "main.py"]
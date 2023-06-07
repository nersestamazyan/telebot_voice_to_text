FROM python:3.8-slim
WORKDIR /opt
COPY requirements.txt /opt
RUN pip install -r requirements.txt
COPY ./ /opt
RUN apt-get update && apt-get install -y cron
CMD ["python3",  "main.py"]
# Dockerfile for Nurse Revenue Pipeline Kafka Producer

FROM python:3.10-slim

WORKDIR /app

COPY kafka/nurse_data_producer.py .

RUN pip install confluent_kafka

CMD ["python", "nurse_data_producer.py"]

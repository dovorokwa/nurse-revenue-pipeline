# nurse_data_producer.py
# Simulate streaming nurse revenue data to Kafka

from confluent_kafka import Producer
import json
import time
import random

p = Producer({'bootstrap.servers': 'your_broker'})

nurses = ["RN001", "EN002", "AEN003"]
departments = ["ICU", "Surgery", "Pediatrics"]

def generate_event():
    return {
        "nurse_id": random.choice(nurses),
        "department": random.choice(departments),
        "net_paid": round(random.uniform(100, 500), 2),
        "net_profit": round(random.uniform(50, 200), 2),
        "timestamp": time.time()
    }

while True:
    event = generate_event()
    p.produce("nurse_revenue_topic", json.dumps(event).encode("utf-8"))
    p.flush()
    time.sleep(1)

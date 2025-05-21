
from fastapi import FastAPI
import requests
import smtplib
import pika
from shared.config import RABBITMQ_URL

app = FastAPI()

@app.get("/check_alerts")
async def check_alerts():
    response = requests.get("http://prediction:8000/predict/123")
    risk_score = response.json()['risk_score']
    if risk_score > 0.7:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('your_email@gmail.com', 'your_password')
            server.sendmail('your_email@gmail.com', 'doctor@example.com',
                            f"Alert: Patient 123 at risk (score: {risk_score})")
        connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
        channel = connection.channel()
        channel.queue_declare(queue='alerts')
        channel.basic_publish(exchange='', routing_key='alerts', body=f"Patient 123: {risk_score}")
        connection.close()
    return {"status": "checked"}
    
import pickle
import os
import mysql.connector

import pika

parameters = pika.URLParameters(os.environ["mq"])
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='NeoQueue')

mydb = mysql.connector.connect(
    host="localhost",
    user="admin", password="Password1", database="emails")
mycursor = mydb.cursor()


def callback(ch, method, properties, body):
    try:
        # SQL Injection
        input_suffix = str(body)[2:-1].split("@", 1)[-1]
        mycursor.execute(f"SELECT * FROM emails WHERE suffix='{input_suffix}';")
    except Exception as e:
        print(f"{e=}")

    try:
        # Deserialization vulnerability
        deserialized = pickle.loads(body)
    except Exception as e:
        print(f"[x] Desrialized data: {body}")

    print(f"[x] Received")


channel.basic_consume(auto_ack=True, on_message_callback=callback, queue="NeoQueue")
channel.start_consuming()

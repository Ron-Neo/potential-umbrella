import pika
import os
from flask import Flask, request, render_template

app = Flask(__name__)
# START DEMO
parameters = pika.URLParameters(os.environ["mq"]) 


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/mq")
def send_to_inner():
    data = request.args.get("data")
    if not data:
        return "500"

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='NeoQueue')
    channel.basic_publish(exchange='', routing_key='NeoQueue', body=data)
    connection.close()
    return "200 OK"


@app.route("/log", methods=['POST'])
def log():
    app.logger.info(str(request.form))
    return str(request.form)


@app.route("/register", methods=['POST'])
def register():
    app.logger.info(str(request.form))
    return str(request.form)

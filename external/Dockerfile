FROM python:3.10.0b2

COPY . /app

# Install python packages
RUN pip install pika
RUN pip install flask

EXPOSE 5000
ENTRYPOINT cd /app; flask run --host=0.0.0.0
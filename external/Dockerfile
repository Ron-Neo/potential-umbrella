FROM python:3.13.11

COPY . /app

# Install python packages
RUN pip install pika
RUN pip install flask

EXPOSE 5000
ENTRYPOINT cd /app; flask run --host=0.0.0.0
FROM python:3.13.11

COPY . /app

# Install python packages
RUN pip install pika mysql-connector-python

ENTRYPOINT cd /app; /usr/local/bin/python main.py
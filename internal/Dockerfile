FROM python:3.14.3

COPY . /app

# Install python packages
RUN pip install pika mysql-connector-python

ENTRYPOINT cd /app; /usr/local/bin/python main.py
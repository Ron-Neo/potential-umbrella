FROM python:3.9

COPY . /app

# Install python packages
RUN pip install pika mysql-connector-python

ENTRYPOINT cd /app; /usr/local/bin/python main.py
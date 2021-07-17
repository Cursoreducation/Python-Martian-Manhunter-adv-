# syntax=docker/dockerfile:1
FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y python python3-pip 
RUN pip install flask
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080


FROM ubuntu:20.04
COPY requirements.txt .
RUN apt-get update && apt-get install -y python python3-pip
RUN pip install -r ./requirements.txt
COPY app.py /opt/
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080

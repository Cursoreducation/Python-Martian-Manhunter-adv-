# pull official base image
FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app/

#RUN pip install flask
#RUN pip install requests

# copy project
COPY . /usr/src/app/

RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
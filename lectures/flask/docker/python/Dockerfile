# pull official base image
FROM python:3.9.5-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app/

RUN pip install flask
# copy project
COPY . /usr/src/app/

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

CMD ["./wait-for-it.sh", "mysql:3306", "--", "gunicorn", "--bind" , "0.0.0.0:5000", "app:app"]
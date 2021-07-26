FROM python:3.9-alpine

RUN pip install django

COPY ./ /app
WORKDIR /app

run ls -la

EXPOSE 8000

CMD python manage.py runserver 0:8000
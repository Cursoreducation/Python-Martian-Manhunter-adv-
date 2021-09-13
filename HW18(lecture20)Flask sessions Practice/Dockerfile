FROM python:3.9.5-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/"

WORKDIR /usr/src/app/

RUN pip install flask

COPY . /usr/src/app/

COPY ./requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

CMD ["./wait-for-it.sh", "mysql:3306", "--", "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

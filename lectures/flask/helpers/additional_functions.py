import datetime
from app import db
from flask import request, session


def check_password(database_password, input_password):
    if database_password == input_password:
        return True
    return False


def log_in(user):
    user.location = request.form.get('location')

    db.session.commit()
    session['user'] = user.serialize

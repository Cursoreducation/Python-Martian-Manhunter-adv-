import os
import tempfile

import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def todos():
    yield {
        "todo_id": 1,
        "text": "text"
    }

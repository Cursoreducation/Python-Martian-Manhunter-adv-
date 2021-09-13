import os
import tempfile
import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

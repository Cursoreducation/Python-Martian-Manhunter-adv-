from http import HTTPStatus

from django.test import TestCase

from django.test import Client

from django.urls import reverse


class StatusViewTests(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('status'))

        assert response.status_code == HTTPStatus.OK

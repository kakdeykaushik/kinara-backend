from django.test import TestCase, Client
from django.urls import reverse
from shortner.models import Url
from users.models import User


# Create your tests here.
import json


class ShortnerTestCase(TestCase):

    def setUp(self):

        self.client = Client()

        user = User.objects.create(username="test_user1", password="pass")
        url = Url.objects.create(original_url="https://www.w3schools.com/PYTHON/ref_requests_get.asp", owner=user)

        self.token = user.get_token().key
        self.test_short_url = url.short_url


    def test_url_view_success(self):

        endpoint = reverse("url-view", args=[self.test_short_url])

        resp = self.client.get(endpoint)

        self.assertEqual(resp.status_code, 302)


    def test_url_view_failure(self):

        params = {
            "url": "1111111"
        }

        endpoint = reverse("url-view", args=[params])

        resp = self.client.get(endpoint, params)

        self.assertEqual(resp.status_code, 404)



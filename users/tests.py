from django.test import TestCase, Client
from django.urls import reverse
from users.models import User

# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):

        self.client = Client()

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        
        self.user = User.objects.create(username= "test_user", password="pass")



    def test_user_register_success(self):
        data = {
            "username": "temp_user",
            "password": "pass"
        }
        resp = self.client.post(self.register_url, data=data)
        data = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(data["token"], str)




    def test_user_register_failure1(self):
        resp = self.client.get(self.register_url)
        self.assertEqual(resp.status_code, 405)




    def test_user_register_failure2(self):
        data = {
            "username": "temp_user",
            # "password": "pass"
        }
        resp = self.client.post(self.register_url, data=data)

        self.assertEqual(resp.status_code, 400)


    def test_user_register_failure3(self):
        data = {
            "username": "test_user",
            "password": "pass"
        }
        resp = self.client.post(self.register_url, data=data)

        self.assertEqual(resp.status_code, 409)



    def test_user_login_success(self):

        data = {
            "username": "test_user",
            "password": "pass"
        }
        resp = self.client.post(self.login_url, data=data)
        data = resp.json()

        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(data["token"], str)




    def test_user_login_failure(self):

        data = {
            "username": "test_user",
            "password": "passss"
        }
        resp = self.client.post(self.login_url, data=data)

        self.assertEqual(resp.status_code, 404)

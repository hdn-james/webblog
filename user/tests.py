from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.


class UserTest(TestCase):
    def setUp(self) -> None:
        self.client = Client(enforce_csrf_checks=True)
        self.urls = {
            'sign_up': reverse('sign_up_view')
        }

    def test_sign_up(self):
        data = {
            'username': 'asdasd',
            'password': '123123'
        }
        response = self.client.post(self.urls['sign_up'], data)
        self.assertEqual(response.status_code, 200)

    def test_one_one_two(self):
        self.assertEqual(1+1, 2)


from django.test import Client
from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from django.test import Client

class URLTests(TestCase):    
    def test_testhomepage(self):
        self.client = Client()
        self.user = User.objects.create_user('Sergej', password='Yaq12wsx!')
        self.client.login(username='Sergej', password='Yaq12wsx!')
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)
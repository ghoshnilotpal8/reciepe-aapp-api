from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse #help us to generate urls for django admin page
from django.test import Client #help us to make test request for our application

class AdminSiteTests(TestCase):               #inheriting TestCase
     def setUp(self):
         self.client = Client()
         self.admin_user = get_user_model().objects.create_superuser(
            email='testemail@beanalytic.com',
            password='beanalytic1234'
         )
         self.client.force_login(self.admin_user)
         self.user = get_user_model().objects.create_user(
            email='testemail@beanalytic.com',
            password='beanalytic1234',
            name='Test user full name'
         )
     def test_users_listed(self):
         """Test that users are listed in user page"""
         url = reverse('admin:core_user_changelist')
         res = self.client.get(url)

         self.assertContains(res, self.user.name)
         self.assertContains(res, self.user.email)

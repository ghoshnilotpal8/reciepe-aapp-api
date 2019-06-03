from django.test import TestCase
from django.contrib.auth import get_user_model


class MedelTests(TestCase):

    def test_create_user_with_successful(self):
        """Test creating a new user with an email in sucessful"""
        email = 'testemail@beanalytic.com'
        password = 'beanalytic1234'
        """calling the create_user function on the user manager on our user model"""
        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email, email) #checks that the email address is correct with the given email address on top
        self.assertTrue(user.check_password(password)) #checks that the password address is correct with the given password address on top


    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'testemail@BEANALYTIC.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@beanalytic.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

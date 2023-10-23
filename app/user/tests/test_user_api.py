from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


USER_CREATE_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(**kwargs):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**kwargs)


class PublicUserApiTests(TestCase):
    """Test public features of the User API."""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating user is successful."""
        payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test Name",
        }
        res = self.client.post(USER_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_create_user_with_existing_email_error(self):
        """Test crating user with existing user's email error."""
        payload = {
            "email": "test@example.com",
            "password": "testpass123",
            "name": "Test Name",
        }
        create_user(**payload)
        res = self.client.post(USER_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error return when password length is less than 5 chars."""
        payload = {
            "email": "test@example.com",
            "password": "test",
            "name": "test user",
        }
        res = self.client.post(USER_CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]).exists()
        self.assertFalse(user_exists)

    def test_create_token_valid_credentials(self):
        """Test creating token for valid credentials."""
        details = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "testpass123",
        }
        create_user(**details)

        payload = {
            "email": details["email"],
            "password": details["password"],
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.data)

    def test_create_token_invalid_credentials_error(self):
        """Test an error for invalid credentials."""
        user_details = {
            "email": "Test@example.com",
            "password": "validpass"
        }
        create_user(**user_details)

        invalid_details = {
            "email": user_details["email"],
            "password": "invalidpass",
        }
        res = self.client.post(TOKEN_URL, invalid_details)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)

    def test_create_token_with_blank_password_error(self):
        """Test an error if password is blank."""
        user_details = {
            "email": "test@example.com",
            "password": "validpass",
        }
        create_user(**user_details)

        payload = {
            "email": user_details["email"],
            "password": ""
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", res.data)

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserManagersTestCase(TestCase):
    def test_create_user(self):
        user_details = {
            "email": "testuser@email.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpass123",
        }

        user = User.objects.create_user(**user_details)

        self.assertEqual(user.email, "testuser@email.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "email": None})

        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "first_name": None})

        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "last_name": None})

        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "password": None})

        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "is_superuser": True})

    def test_create_superuser(self):
        superuser_details = {
            "email": "superuser@email.com",
            "first_name": "Super",
            "last_name": "User",
            "password": "testpass123",
        }

        superuser = User.objects.create_superuser(**superuser_details)

        self.assertEqual(superuser.email, superuser_details["email"])
        self.assertEqual(superuser.first_name, superuser_details["first_name"])
        self.assertEqual(superuser.last_name, superuser_details["last_name"])
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(**{**superuser_details, "is_staff": False})

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                **{**superuser_details, "is_superuser": False}
            )

        with self.assertRaises(ValueError):
            User.objects.create_superuser(**{**superuser_details, "is_active": False})

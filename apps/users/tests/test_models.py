from django.contrib.auth import get_user_model
from django.test import TestCase

from .factories import UserFactory


class UserModelsTestCase(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.u = UserFactory()
        self.user = User.objects.get(id=self.u.id)

    def test_str_method(self):
        self.assertEqual(str(self.user), self.u.email)

    def test_full_name_property(self):
        self.assertEqual(self.user.full_name, f"{self.u.first_name} {self.u.last_name}")

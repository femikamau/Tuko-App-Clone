import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model.

    Extends the base `AbstractBaseUser` and `PermissionsMixin`.
    Uses the `email` as unique identifier for authentication.
    The user `first_name`, `last_name` are also required.
    """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False)

    email = models.EmailField(_("email address"), unique=True, blank=False)
    first_name = models.CharField(_("first name"), max_length=30, blank=False)
    last_name = models.CharField(_("last name"), max_length=30, blank=False)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.email}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

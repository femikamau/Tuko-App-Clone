from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom User Model Manager
    """

    def _create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Create and save a User with the given email, first name, last name and password.
        """

        if not email:
            raise ValueError("The email must be set")

        if not first_name:
            raise ValueError("The first name must be set")

        if not last_name:
            raise ValueError("The last name must be set")

        if not password:
            raise ValueError("The password must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Create and save a regular User with the given email, first name,
        last name and password.
        """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if extra_fields.get("is_superuser") is True:
            raise ValueError("Regular users must not be superusers")

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Create and save a Superuser with the given email, first name,
        last name and password.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is False:
            raise ValueError("Superusers must be staff")

        if extra_fields.get("is_superuser") is False:
            raise ValueError("Superusers must be superusers")

        if extra_fields.get("is_active") is False:
            raise ValueError("Superusers must be active")

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )

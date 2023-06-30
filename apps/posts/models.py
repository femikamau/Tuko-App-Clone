import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Post(models.Model):
    """
    News Post Model
    """

    class StatusChoices(models.TextChoices):
        """
        Status Choices
        """

        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Published")

    uuid = models.UUIDField(_("uuid"), default=uuid.uuid4, editable=False)

    headline = models.CharField(_("headline"), max_length=255, blank=False)
    content = models.TextField(_("content"), blank=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")
    image = models.ImageField(_("image"), upload_to="posts", blank=True, null=True)
    status = models.CharField(
        _("status"),
        max_length=9,
        choices=StatusChoices.choices,
        blank=False,
    )
    published_at = models.DateTimeField(_("published at"), blank=True, null=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.headline

    @classmethod
    def get_published_posts(cls):
        """
        Get published posts
        """
        return cls.objects.filter(status=cls.StatusChoices.PUBLISHED)

from django.test import TestCase

from apps.posts.models import Post
from apps.users.tests.factories import UserFactory


class PostModelsTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()

    def test_draft_post(self):
        post = Post.objects.create(
            headline="Test Headline",
            content="Test Content",
            author=self.user,
            status=Post.StatusChoices.DRAFT,
        )

        self.assertEqual(str(post), post.headline)
        self.assertEqual(post.published_at, None)
        self.assertEqual(Post.get_published_posts().count(), 0)

    def test_published_post(self):
        post = Post.objects.create(
            headline="Test Headline",
            content="Test Content",
            author=self.user,
            status=Post.StatusChoices.PUBLISHED,
        )

        self.assertEqual(str(post), post.headline)
        self.assertNotEqual(post.published_at, None)
        self.assertEqual(Post.get_published_posts().count(), 1)

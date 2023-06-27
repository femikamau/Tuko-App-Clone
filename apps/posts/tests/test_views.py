from django.test import TestCase
from rest_framework.test import APIClient

from apps.posts.models import Post
from apps.users.tests.factories import UserFactory


class PostViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        post = Post.objects.create(
            headline="test", content="test", author=self.user, status="published"
        )
        self.post = post

    def test_post_list(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_detail(self):
        response = self.client.get(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["headline"], self.post.headline)

    def test_post_create(self):
        response = self.client.post(
            "/api/posts/",
            {"headline": "test", "content": "test", "status": "published"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["headline"], "test")

    def test_post_update(self):
        response = self.client.put(
            f"/api/posts/{self.post.id}/",
            {"headline": "test", "content": "test", "status": "published"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["headline"], "test")

    def test_post_delete(self):
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)

import datetime

from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Post
from .serializers import ReadPostSerializer, WritePostSerializer


class PostViewSet(ModelViewSet):
    """
    Post ViewSet
    """

    queryset = Post.objects.all()
    serializer_class = WritePostSerializer

    def create(self, request, *args, **kwargs):
        # Only authenticated users can create posts
        if request.user.is_authenticated:
            return super().create(request, *args, **kwargs)

        # Otherwise, return a 401
        return Response(
            data={"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        # If the status is published, set the published_at field to the current time
        if serializer.validated_data.get("status") == Post.StatusChoices.PUBLISHED:
            serializer.instance.published_at = datetime.datetime.now()
            serializer.instance.save()

        # If the status is draft, set the published_at field to None
        elif serializer.validated_data.get("status") == Post.StatusChoices.DRAFT:
            serializer.instance.published_at = None
            serializer.instance.save()

    def list(self, request, *args, **kwargs):
        # If the user is authenticated, display all their posts
        if request.user.is_authenticated:
            self.queryset = request.user.posts.all()
            return super().list(request, *args, **kwargs)

        # Otherwise, return a 401
        return Response(
            data={"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def retrieve(self, request, *args, **kwargs):
        post = self.get_object()

        # If the user is the author of the post, display the post
        if post.author == request.user or post.status == Post.StatusChoices.PUBLISHED:
            return super().retrieve(request, *args, **kwargs)

        # Otherwise, return a 404
        return Response(
            data={"detail": "Not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    def update(self, request, *args, **kwargs):
        post = self.get_object()

        # Only the author can update their post
        if post.author == request.user:
            # Check if the status is being changed to published
            if request.data.get("status") == Post.StatusChoices.PUBLISHED:
                # Check if the post has been published before
                if post.published_at is None:
                    # If it hasn't, set the published_at field to the current time
                    post.published_at = datetime.datetime.now()

            return super().update(request, *args, **kwargs)

        # Otherwise, return a 403
        return Response(
            data={"detail": "You do not have permission to edit this post"},
            status=status.HTTP_403_FORBIDDEN,
        )

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()

        # Only the author or an admin user can delete the post
        if post.author == request.user or request.user.is_staff:
            return super().destroy(request, *args, **kwargs)

        # Otherwise, return a 403
        return Response(
            data={"detail": "You do not have permission to delete this post"},
            status=status.HTTP_403_FORBIDDEN,
        )


class FeedViewSet(ListModelMixin, GenericViewSet):
    """
    Feed ViewSet
    """

    queryset = Post.get_published_posts()
    serializer_class = ReadPostSerializer
    permission_classes = (AllowAny,)

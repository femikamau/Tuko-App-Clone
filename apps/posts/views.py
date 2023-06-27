from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


class PostCreateView(CreateView):
    form_class = PostForm
    # template_name =
    # success_url = "/"
    # success_message = "Post created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostViewSet(ModelViewSet):
    """
    Post ViewSet.
    """

    queryset = Post.get_published_posts()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user and not request.user.is_superuser:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        return super().destroy(request, *args, **kwargs)

from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer.
    """

    url = serializers.HyperlinkedIdentityField(view_name="post-detail")

    author = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="user-detail"
    )

    class Meta:
        model = Post
        fields = ("id", "url", "headline", "content", "image", "status", "author")
        read_only_fields = ("id", "author")

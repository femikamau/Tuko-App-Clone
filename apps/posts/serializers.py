from rest_framework import serializers

from .models import Post


class ReadPostSerializer(serializers.ModelSerializer):
    """
    Read Post Serializer

    To be applied on views that have read-only functionality
    """

    url = serializers.HyperlinkedIdentityField(view_name="post-detail")

    author = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="full_name"
    )

    class Meta:
        model = Post
        fields = (
            "url",
            "headline",
            "content",
            "image",
            "author",
            "published_at",
        )
        read_only_fields = ("published_at",)


class WritePostSerializer(ReadPostSerializer):
    """
    Write Post Serializer

    Extends the `ReadPostSerializer`.
    To be applied on views that have `Create`, `Read`, `Update`, and `Delete`
    functionality

    Adds `status` to the fields
    """

    class Meta(ReadPostSerializer.Meta):
        fields = ReadPostSerializer.Meta.fields + ("status",)

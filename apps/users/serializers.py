from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    posts = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="post-detail"
    )

    class Meta:
        model = User
        fields = (
            "id",
            "url",
            "email",
            "first_name",
            "last_name",
            "posts",
        )

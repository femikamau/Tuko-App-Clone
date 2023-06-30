from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apps.posts.views import FeedViewSet, PostViewSet
from apps.users.views import RegisterView, UserViewSet

router = DefaultRouter()

router.register(prefix=r"users", viewset=UserViewSet, basename="user")
router.register(prefix=r"feed", viewset=FeedViewSet, basename="feed")
router.register(prefix=r"posts", viewset=PostViewSet, basename="post")

urlpatterns = [
    path(route="register/", view=RegisterView.as_view(), name="register"),
    path(route="login/", view=obtain_auth_token),
    path(route="rest-auth/", view=include("rest_framework.urls")),
] + router.urls

from django.shortcuts import render
from django.views.generic import CreateView

from .forms import PostForm


class PostCreateView(CreateView):
    form_class = PostForm
    # template_name =
    # success_url = "/"
    # success_message = "Post created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

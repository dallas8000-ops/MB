from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Class-based views for posts
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = "posts"

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "author"]
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        # Set the author to the last user (if using User model, otherwise remove this line)
        # from django.contrib.auth.models import User
        # form.instance.author = User.objects.last()
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    success_url = reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

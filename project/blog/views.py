from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.contrib.auth.models import User

# User = get_user_model()

# # dummy posts from db
# posts = [
#     {
#         "author": "Mehedi Ehteshum",
#         "title": "Post 1",
#         "content": "This is the first post.",
#         "date_posted": "January 1, 2021"
#     },
#     {
#         "author": "Mansura Khanom",
#         "title": "Post 2",
#         "content": "This is the second post.",
#         "date_posted": "January 3, 2021"
#     }
# ]

# Create your views here.
## FBV of home page
# def home(request):
#     posts = reversed(Post.objects.all())
#     context = {
#         "title": "Home",
#         "posts": posts
#     }
#     return render(request, "blog/home.html", context)

# CBV of home page
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html" # default: app/model_viewtype.html -> blog/post_list.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 3

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/user_posts.html" # default: app/model_viewtype.html -> blog/post_list.html
    context_object_name = "posts"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request, "blog/about.html")

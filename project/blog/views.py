from django.shortcuts import render

# dummy posts from db
posts = [
    {
        "author": "Mehedi Ehteshum",
        "title": "Post 1",
        "content": "This is the first post.",
        "date_posted": "January 1, 2021"
    },
    {
        "author": "Mansura Khanom",
        "title": "Post 2",
        "content": "This is the second post.",
        "date_posted": "January 3, 2021"
    },
    {
        "author": "Md Azim",
        "title": "Post 3",
        "content": "HTML khub moja.",
        "date_posted": "January 3, 2021"
    }
]

# Create your views here.
def home(request):
    context = {
        "title": "Home",
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")

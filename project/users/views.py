from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save() # creates and saves user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("blog-home")
    else:
        form = UserSignupForm()
    context = {"form": form}
    return render(request, "users/signup.html", context)

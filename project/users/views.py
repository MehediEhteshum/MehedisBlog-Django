from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save() # creates and saves user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You can now sign in.")
            return redirect("user-signin")
    else:
        form = UserSignupForm()
    context = {"form": form}
    return render(request, "users/signup.html", context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')

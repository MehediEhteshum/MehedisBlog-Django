"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from blog.views import (
    # home,
    PostListView,
    UserPostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about,
)
from users.views import(
    signup,
    profile
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name="blog-home"),
    path('user-profile/', profile, name="user-profile"),  
    path('<str:username>-posts/', UserPostListView.as_view(), name="userposts-list"),
    path('post-<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('new-post/', PostCreateView.as_view(), name="post-create"),
    path('post-<int:pk>/update', PostUpdateView.as_view(), name="post-update"),
    path('post-<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('about/', about, name="blog-about"),
    path('signup/', signup, name="user-signup"),
    path('signin/', LoginView.as_view(template_name="users/signin.html"), name="user-signin"),
    path('signout/', LogoutView.as_view(template_name="users/signout.html"), name="user-signout"),
    path('password-reset/', PasswordResetView.as_view(template_name="users/password_reset.html"), name="password-reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password-reset-done"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

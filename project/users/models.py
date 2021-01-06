from django.db import models
from django.conf import settings
from PIL import Image

User = settings.AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        max_dim = 300
        if img.width>max_dim or img.height>max_dim:
            output_size = (max_dim, max_dim)
            img.thumbnail(output_size)
            img.save(self.image.path)


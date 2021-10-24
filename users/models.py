from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300)
    image = models.ImageField(
        default='profile_default.png', upload_to='profile_pics')

    def __str__(self):
        return f'Perfil do {self.user.username}'

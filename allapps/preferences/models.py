from django.db import models
from ..songs.models import Song
from django.contrib.auth import get_user_model


# Create your models here.
class Preference(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    songs = models.ManyToManyField(Song, related_name='songs')
    date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} - {self.active}'

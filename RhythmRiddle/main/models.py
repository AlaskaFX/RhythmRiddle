from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

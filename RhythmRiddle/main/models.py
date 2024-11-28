
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Song(models.Model):
    SONG_GENRE = [
        ('rock', 'Рок'),
        ('romance', 'Шансон'),
        ('disco', 'Диско'),
        ('dance', 'Танец'),
        ('pop', 'Поп'),
        ('rap', 'Рэп'),
        ('house', 'Хаус'),
        ('edm', 'Электро'),
        ('bandstand', 'Эстрада'),
    ]

    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    song_genre = models.CharField(max_length=10, choices=SONG_GENRE, null=True, blank=True)
    file = models.FileField(upload_to='full_songs/')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'

class Quiz(models.Model):
    QUIZ_TYPE_CHOICES = [
        ('title', 'Название'),
        ('composer', 'Композитор'),
        ('genre', 'Жанр'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Легко'),
        ('hard', 'Сложно'),
    ]

    title = models.CharField(max_length=255)
    quiz_type = models.CharField(max_length=10, choices=QUIZ_TYPE_CHOICES)
    difficulty = models.CharField(max_length=4, choices=DIFFICULTY_CHOICES)
    song_file = models.FileField(upload_to='short_songs/')
    correct_answer = models.CharField(max_length=255)
    wrong_answer1 = models.CharField(max_length=255)
    wrong_answer2 = models.CharField(max_length=255)
    wrong_answer3 = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'


class Stats(models.Model):
    USERS_GENRE = [
        ('rock', 'Рок'),
        ('romance', 'Шансон'),
        ('disco', 'Диско'),
        ('dance', 'Танец'),
        ('pop', 'Поп'),
        ('rap', 'Рэп'),
        ('house', 'Хаус'),
        ('edm', 'Электро'),
        ('bandstand', 'Эстрада'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=100)
    attempts = models.IntegerField(default=3)
    last_reset_date = models.DateField(auto_now=True)
    user_genre = models.CharField(max_length=10, choices=USERS_GENRE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.last_reset_date != timezone.now().date():
            self.attempts = 3
            self.last_reset_date = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Stats for {self.user.username}'

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'song')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f"{self.user.username} - {self.song.title}"
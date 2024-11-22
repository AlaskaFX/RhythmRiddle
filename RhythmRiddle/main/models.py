
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    file = models.FileField(upload_to='songs/')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"

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

    title = models.CharField(max_length=255)  # Название мелодии
    quiz_type = models.CharField(max_length=10, choices=QUIZ_TYPE_CHOICES)  # Тип задания
    difficulty = models.CharField(max_length=4, choices=DIFFICULTY_CHOICES)  # Сложность
    song_file = models.FileField(upload_to='songs/')  # Выбор песни (файлом)
    correct_answer = models.CharField(max_length=255)  # Правильный ответ
    wrong_answer1 = models.CharField(max_length=255)  # Неправильный ответ 1
    wrong_answer2 = models.CharField(max_length=255)  # Неправильный ответ 2
    wrong_answer3 = models.CharField(max_length=255)  # Неправильный ответ 3

    def __str__(self):
        return self.title


class Stats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Логин пользователя
    points = models.IntegerField(default=100)  # Баллы по умолчанию
    attempts = models.IntegerField(default=3)  # Количество попыток по умолчанию
    last_reset_date = models.DateField(auto_now=True)  # Дата последнего сброса

    def save(self, *args, **kwargs):
        # Сбрасываем количество попыток в начале нового дня
        if self.last_reset_date != timezone.now().date():
            self.attempts = 3
            self.last_reset_date = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Stats for {self.user.username}'

# Generated by Django 5.1.3 on 2024-11-29 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_song_song_genre_alter_stats_user_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='play_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

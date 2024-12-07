
from django.contrib import admin
from .models import Song, Quiz, Stats, FavoriteSong, Playlist

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'song_genre', 'play_count')
    exclude = ('play_count',)

class StatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_user_genre', 'second_user_genre', 'third_user_genre')

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiz_type', 'difficulty', 'correct_answer')

admin.site.register(Song, SongAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(FavoriteSong)
admin.site.register(Playlist)
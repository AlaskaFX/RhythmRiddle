
from django.contrib import admin
from .models import Song, Quiz, Stats, FavoriteSong

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'song_genre')

admin.site.register(Song, SongAdmin)
admin.site.register(Quiz)
admin.site.register(Stats)
admin.site.register(FavoriteSong)
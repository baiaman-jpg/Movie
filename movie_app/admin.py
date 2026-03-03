from django.contrib import admin
from .models import *



class MovieLanguageInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1

class MomentsInline(admin.TabularInline):
    model = Moments
    extra = 1

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguageInline, MomentsInline]

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(History)
admin.site.register(ReviewLike)
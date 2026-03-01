from django.contrib import admin
from .models import Genre, Actor, Movie, Review



class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    fields = ("name", "rating", "text", "created_at")
    readonly_fields = ("created_at",)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_year")
    list_filter = ("release_year", "genre")
    search_fields = ("title",)
    filter_horizontal = ("genre", "actors")
    inlines = [ReviewInline]



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie", "name", "rating", "created_at")
    list_filter = ("rating", "created_at")
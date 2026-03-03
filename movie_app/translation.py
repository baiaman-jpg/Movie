from .models import Director, Actor, Genre, Movie, Rating, Review, Category
from modeltranslation.translator import TranslationOptions, register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Director)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('director_name','director_bio')


@register(Actor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'actor_bio')

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')

@register(Rating)
class RatingTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('text',)
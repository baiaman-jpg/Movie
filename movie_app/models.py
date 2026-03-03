from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


STATUS_CHOICES = (
    ('simple', 'Simple'),
    ('middle', 'Middle'),
    ('top', 'Top'),
)


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(85)],
        null=True,
        blank=True
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        region="RU"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='simple'
    )
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=64)
    director_bio = models.TextField(null=True, blank=True)
    director_age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(15), MaxValueValidator(85)],
        null=True,
        blank=True
    )
    director_image = models.ImageField(upload_to="director_images/", null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    actor_bio = models.TextField(null=True, blank=True)
    actor_age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        null=True,
        blank=True
    )
    actor_image = models.ImageField(upload_to='actor_photo/', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=64)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='genres'
    )

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    TYPES_CHOICES = (
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080', '1080'),
        ('1080_ULTRA', '1080 ULTRA'),
    )

    movie_name = models.CharField(max_length=64)
    year = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='movies')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='movies')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')

    types = models.CharField(max_length=20, choices=TYPES_CHOICES, default='720')
    movie_time = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.URLField()
    movie_image = models.ImageField(upload_to="movie_photo/", null=True, blank=True)
    status_movie = models.CharField(max_length=20, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.movie_name


class MovieLanguages(models.Model):
    language = models.CharField(max_length=32)
    video = models.FileField(upload_to="movie_video/")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return f"{self.movie.movie_name} - {self.language}"


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments')
    movie_moments = models.ImageField(upload_to="movie_moments/", null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)],
        null=True,
        blank=True
    )
    text = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name}"


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name}"


class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review_likes')

    class Meta:
        unique_together = ('review', 'user')


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.user.username


class FavoriteMovie(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_in')

    class Meta:
        unique_together = ('favorite', 'movie')


class History(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='history')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='viewed_history')
    viewed_at = models.DateTimeField(auto_now_add=True)
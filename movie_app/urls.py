from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter
from .views import (
    UserProfileViewSet, CategoryViewSet, CountryViewSet,
    DirectorViewSet, ActorViewSet, GenreViewSet,
    MovieDetailAPIView, MovieListAPIView, MovieLanguagesViewSet, MomentsViewSet,
    RatingViewSet, ReviewViewSet, ReviewLikeViewSet,
    FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, LoginView, LogoutView, RegisterView
)

router = SimpleRouter()

router.register(r'users', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'directors', DirectorViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'movie-languages', MovieLanguagesViewSet)
router.register(r'moments', MomentsViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'review-likes', ReviewLikeViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-movies', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)
schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('movie/', MovieListAPIView.as_view() , name='movie_list'),
    path('movie/<int:pk>', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

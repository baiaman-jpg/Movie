
from django_filters.rest_framework import FilterSet
from .models import *



class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year' :[ 'gte', 'lte' ],
            'country' :[ 'exact'],
            'director': ['exact' ],
            'actor': ['exact' ],
            'genre': ['exact' ],
            'status_movie': ['exact' ],
        }

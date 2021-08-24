from rest_framework import ( viewsets, permissions )
from rest_framework.decorators import api_view


from .serializers import (
    CocktailSerializer,
    FeastSerializer,
)
from .models import (
    Feast,
    Cocktail,
    CocktailIngredient,
    Ingredient,
)


class CocktailViewSet(viewsets.ReadOnlyModelViewSet):
    '''
        API Endpoint for Cocktails
    '''
    queryset = Cocktail.objects.all().order_by('name')
    serializer_class = CocktailSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeastViewSet(viewsets.ReadOnlyModelViewSet):
     '''
        API Endpoint for Feasts
     '''
     queryset = Feast.objects.all().order_by('date')
     serializer_class = FeastSerializer
     permission_classes = [permissions.IsAuthenticated]

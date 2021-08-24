from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import (
    CocktailViewSet,
    FeastViewSet,
)

router = routers.DefaultRouter()
router.register('feasts', FeastViewSet)
router.register('cocktails', CocktailViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

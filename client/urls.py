from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path("", include("django_nextjs.urls")),
]

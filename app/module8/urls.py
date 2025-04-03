# module8/urls.py
from inspect import getmembers, isclass

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

from . import views

# Set up a router and register our viewset
router = DefaultRouter()
# router.register(r'categories', CategoryInsertViewSet, basename='category')
# Automatically find all ViewSets in views.py and register them
for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        router.register(
            rf"{name.lower().replace('viewset', '')}", cls, basename=name.lower()
        )

urlpatterns = [
    path("api/mod8/", include(router.urls)),  # Register the routes under '/api/m4/'
]

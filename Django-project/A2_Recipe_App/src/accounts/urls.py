from django.urls import path
from . import views
from .views import favorite_add

app_name = "accounts"

urlpatterns = [
    path("fav/<int:id>/", views.favorite_add, name="favorite_add")
    ]

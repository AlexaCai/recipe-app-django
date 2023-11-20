from django.urls import path
from . import views
from .views import favorite_add, delete_recipe, user_private_recipe_new

app_name = "accounts"

urlpatterns = [
    path("fav/<int:id>/", views.favorite_add, name="favorite_add"),
    path("delete/<int:id>/", views.delete_recipe, name="delete_recipe"),
    path('recipe/new/', views.user_private_recipe_new, name='user_private_recipe_new')
    ]

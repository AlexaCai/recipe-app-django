from django.urls import path
from .views import (
    favorite_add,
    delete_recipe,
    user_private_recipe_new,
    signup_view,
    login_view,
    logout_view,
    profile_view,
)

app_name = "accounts"

urlpatterns = [
    path("fav/<int:id>/", favorite_add, name="favorite_add"),
    path("delete/<int:id>/", delete_recipe, name="delete_recipe"),
    path("recipe/new/", user_private_recipe_new, name="user_private_recipe_new"),
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
]

from django.urls import path
from django.views.generic import TemplateView
from .views import (
    home,
    unsigned_user_redirect_recipes_list_page,
    signed_user_redirect_recipes_list_page,
    unsigned_user_redirect_recipes_detailed_page,
    signed_user_redirect_recipes_detailed_page,
    search_recipes_by_name,
    search_recipes_by_filters,
    search_recipes_by_ingredients,
    publish_comment,
    delete_comment,
    update_comment,
    user_submit_recipe,
)

app_name = "recipes"

urlpatterns = [
    path("", home),
    path("home/", 
         home, 
         name="home"
    ),
    path(
        "recipes-list-unsigned-users/",
        unsigned_user_redirect_recipes_list_page,
        name="recipes_list_unsigned_users",
    ),
    path(
        "recipes-list-signed-users/",
        signed_user_redirect_recipes_list_page,
        name="recipes_list_signed_users",
    ),
    path(
        "recipes-submit/",
        user_submit_recipe,
        name="user_submit_recipe",
    ),
    path(
        "recipe_submitted_success.html",
        TemplateView.as_view(template_name="recipes/recipe_submitted_success.html"),
        name="user_submitted_recipe_success",
    ),
    path(
        "recipe_submitted_failed.html",
        TemplateView.as_view(template_name="recipes/recipe_submitted_failed.html"),
        name="user_submitted_recipe_failed",
    ),
    path("search-recipe-name/", 
         search_recipes_by_name, 
         name="search_recipes_name"
    ),
    path(
        "search-recipe-filters/",
        search_recipes_by_filters,
        name="search_recipes_filters",
    ),
    path(
        "search-recipe-ingredients/",
        search_recipes_by_ingredients,
        name="search_recipes_ingredients",
    ),
    path(
        "recipes-detail-unsigned-users/<pk>",
        unsigned_user_redirect_recipes_detailed_page,
        name="recipes_detail_unsigned_users",
    ),
    path(
        "recipes-detail-signed-users/<pk>",
        signed_user_redirect_recipes_detailed_page,
        name="recipes_detail_signed_users",
    ),
    path("publish-comment/<int:pk>/", 
         publish_comment, 
         name="publish_comment"
    ),
    path("delete-comment/<int:id>/", 
     delete_comment, 
         name="delete_comment"
    ),
    path("update-comment/<int:id>/", 
         update_comment, 
         name="update_comment"
    ),
]

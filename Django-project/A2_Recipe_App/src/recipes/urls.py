from django.urls import path
from .views import home, unsigned_user_redirect_recipes_list_page, signed_user_redirect_recipes_list_page, unsigned_user_redirect_recipes_detailed_page, signed_user_redirect_recipes_detailed_page, search_recipes_by_name, search_recipes_by_filters, search_recipes_by_ingredients, publish_comment

app_name = "recipes"

urlpatterns = [
    path("", home),
    path('home/', home, name='home'),
    path('recipes-list-unsigned-users/', unsigned_user_redirect_recipes_list_page, name='recipes_list_unsigned_users'),
    path('recipes-list-signed-users/', signed_user_redirect_recipes_list_page, name='recipes_list_signed_users'),
    path('search-recipe-name/', search_recipes_by_name, name='search_recipes_name'),
    path('search-recipe-filters/', search_recipes_by_filters, name='search_recipes_filters'),
    path('search-recipe-ingredients/', search_recipes_by_ingredients, name='search_recipes_ingredients'),
    path('recipes-detail-unsigned-users/<pk>', unsigned_user_redirect_recipes_detailed_page, name='recipes_detail_unsigned_users'),
    path('recipes-detail-signed-users/<pk>', signed_user_redirect_recipes_detailed_page, name='recipes_detail_signed_users'),
    path("publish-comment/<int:pk>/", publish_comment, name="publish_comment"),
]

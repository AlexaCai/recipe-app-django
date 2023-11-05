from django.urls import path
from . import views
from .views import home, search_recipes_by_name, search_recipes_by_filters, search_recipes_by_ingredients, RecipeListViewUnsignedUsers, RecipeListViewSignedUsers, RecipeDetailViewUnsignedUsers, RecipeDetailViewSignedUsers

app_name = "recipes"

urlpatterns = [
    path("", home),
    path('home/', home, name='home'),
    path('recipes-list-unsigned-users/', RecipeListViewUnsignedUsers.as_view(), name='recipes_list_unsigned_users'),
    path('recipes-list-signed-users/', RecipeListViewSignedUsers.as_view(), name='recipes_list_signed_users'),
    path('search-recipe-name/', search_recipes_by_name, name='search_recipes_name'),
    path('search-recipe-filters/', search_recipes_by_filters, name='search_recipes_filters'),
    path('search-recipe-ingredients/', search_recipes_by_ingredients, name='search_recipes_ingredients'),
    path('recipes-detail-unsigned-users/<pk>', RecipeDetailViewUnsignedUsers.as_view(), name='recipes_detail_unsigned_users'),
    path('recipes-detail-signed-users/<pk>', RecipeDetailViewSignedUsers.as_view(), name='recipes_detail_signed_users')

]

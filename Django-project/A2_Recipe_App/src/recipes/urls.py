from django.urls import path
from . import views
from .views import home, search_recipes, RecipeListView

app_name = "recipes"

# Since we want to have a custom homepage instead of the default Django welcome page when \
# 'http://127.0.0.1:8000/' is visited, and since nothing is written after the main \
# 'http://127.0.0.1:8000/' URL, the route parameter is currently empty '' in (path('', ...)).
# This specifies that when 'http://127.0.0.1:8000/' is visited, the page specified by \
# home will be seen, rather than the default Django welcome page.
urlpatterns = [
    path("", home),
    path('home/', home, name='home'),
    path('recipes-list-unsigned-users/', RecipeListView.as_view(), name='recipes-list-unsigned-users'),
    path('search-recipe-name/', search_recipes, name='search_recipes-name'),
]

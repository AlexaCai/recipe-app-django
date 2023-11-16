from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from recipes.models import Recipe

# Used to display recipes that are favorited by the user.
def favorite_list(request):
    favorites = request.user.favorites.all()
    print(f'These are the favorites: {favorites}')

    favorite_recipes = Recipe.objects.filter(favorites=request.user)
    print(f'These are the new favorites: {favorite_recipes}')

    return favorite_recipes

# Used to add or remove recipes from the user's favorites.
def favorite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
        print(f'Recipe removed from favorites. Recipe ID: {id}, User: {request.user}, User_ID: {request.user.id}')
    else:
        recipe.favorites.add(request.user)
        print(f'Recipe added to favorites. Recipe ID: {id}, User: {request.user}, User_ID: {request.user.id}')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

# Used to display recipes that are favorited by the user.
def created_recipe(request):
    created_recipes = request.user.created_recipes.all()
    print(f'These are the user created recipes: {created_recipes}')
    return created_recipes




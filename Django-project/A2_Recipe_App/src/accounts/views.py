from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from recipes.models import Recipe

# Used to display recipes that are favorited by the user.
def favorite_list(request):
    favorites = request.user.favorites.all()
    print(f'These are the favorites: {favorites}')

    new = Recipe.objects.filter(favorites=request.user)
    print(f'These are the new favorites: {new}')

    return render(request, 'accounts/profile.html', {'new': new})

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

# Used to determined if a recipe is in the user's favorites, and update the ''add to favorites'' button accordingly.
def detailed_recipe_view(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    print('This is the recipe: ', recipe)

    is_favorite = recipe.favorites.filter(id=request.user.id).exists()
    print('This is the is_favorite: ', is_favorite)

    return render(request, 'your_template.html', {'recipe': recipe, 'is_favorite': is_favorite})
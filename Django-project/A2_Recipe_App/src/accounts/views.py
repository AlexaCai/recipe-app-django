from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from recipes.models import Recipe
from .forms import UserCreatePrivateRecipe, RecipeIngredientsFormSet, RecipeAllergensFormSet, RecipeCookingInstructionsFormSet

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

# Used to display recipes that are favorited by the user.
def created_recipe(request):
    created_recipes = request.user.created_recipes.all()
    print(f'These are the user created recipes: {created_recipes}')
    return created_recipes

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def user_private_recipe_new(request):
    if request.method == "POST":
        form = UserCreatePrivateRecipe(request.POST, request.FILES)
        formset = RecipeIngredientsFormSet(request.POST, prefix='formset')
        allergens_formset = RecipeAllergensFormSet(request.POST, prefix='allergens')
        cooking_instructions_formset = RecipeCookingInstructionsFormSet(request.POST, prefix='cooking_instructions')

        if form.is_valid() and formset.is_valid() and allergens_formset.is_valid() and cooking_instructions_formset.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            formset.instance = recipe
            formset.save()

            allergens_formset.instance = recipe
            allergens_formset.save()

            cooking_instructions_formset.instance = recipe
            cooking_instructions_formset.save()

            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            print(formset.errors)
            print(allergens_formset.errors)
            print(cooking_instructions_formset.errors)

    else:
        form = UserCreatePrivateRecipe()
        formset = RecipeIngredientsFormSet(prefix='formset')
        allergens_formset = RecipeAllergensFormSet(prefix='allergens')
        cooking_instructions_formset = RecipeCookingInstructionsFormSet(prefix='cooking_instructions')

    return render(request, 'accounts/profile.html', {'form': form, 'formset': formset, 'allergens_formset': allergens_formset, 'cooking_instructions_formset': cooking_instructions_formset})


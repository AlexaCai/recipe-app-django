from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login, logout
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserAdminCreationForm  
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from recipes.models import Recipe, RecipeIngredients
from .forms import UserCreatePrivateRecipe, RecipeIngredientsFormSet, RecipeAllergensFormSet, RecipeCookingInstructionsFormSet
from django.urls import reverse

def signup_view(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)  # Use the custom form
        if form.is_valid():
            form.save()
            print("User created successfully")
            return redirect('accounts:login')
        else:
            print("User creation failed")
            print(form.errors)
    else:
        form = UserAdminCreationForm()  # Use the custom form

    return render(request, 'accounts/signup.html', {'form': form})


# define a function view called login_view that takes a request from user
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("recipes:recipes_list_signed_users")
        else:
            error_message = "ooops.. something went wrong"

    # prepare data to send from view to template
    context = {"form": form, "error_message": error_message}
    return render(request, "accounts/login.html", context)


# define a function view called logout_view that takes a request from user
def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def delete_account(request):
    user = request.user
    user.delete()
    return render(request, 'accounts/account-deleted.html')


# Allow to display the user's profile page.
def profile_view(request):
    favorite_recipes = favorite_list(request)
    created_recipes = created_recipe(request)
    form = UserCreatePrivateRecipe()
    formset = RecipeIngredientsFormSet(prefix='formset')
    allergens_formset = RecipeAllergensFormSet(prefix='allergens')
    cooking_instructions_formset = RecipeCookingInstructionsFormSet(prefix='cooking_instructions')

    return render(
        request,
        'accounts/profile.html',
        {
            'favorite_recipes': favorite_recipes,
            'created_recipes': created_recipes,
            'form': form,
            'formset': formset,
            'allergens_formset': allergens_formset,
            'cooking_instructions_formset': cooking_instructions_formset,
        }
    )

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
def favorite_list(request):
    favorites = request.user.favorites.all()
    print(f'These are the favorites: {favorites}')

    favorite_recipes = Recipe.objects.filter(favorites=request.user)
    print(f'These are the new favorites: {favorite_recipes}')

    return favorite_recipes


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

        print("Form Data:", request.POST)
        print("Form Files:", request.FILES)
        print("Formset Data:", formset.data)
        print("Allergens Formset Data:", allergens_formset.data)
        print("Cooking Instructions Formset Data:", cooking_instructions_formset.data)

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


def user_private_recipe_update(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = UserCreatePrivateRecipe(request.POST, request.FILES, instance=recipe)
        formset = RecipeIngredientsFormSet(request.POST, prefix='formset', queryset=RecipeIngredients.objects.filter(recipe=recipe), instance=recipe)
        allergens_formset = RecipeAllergensFormSet(request.POST, prefix='allergens', instance=recipe)
        cooking_instructions_formset = RecipeCookingInstructionsFormSet(request.POST, prefix='cooking_instructions', instance=recipe)

        if form.is_valid() and formset.is_valid() and allergens_formset.is_valid() and cooking_instructions_formset.is_valid():
            form.save()
            formset.save()
            allergens_formset.save()
            cooking_instructions_formset.save()

            for form in formset:
                print(f"Form ID: {form.instance.id}")

            return redirect('accounts:profile')
    else:
        form = UserCreatePrivateRecipe(instance=recipe)
        formset = RecipeIngredientsFormSet(prefix='formset', queryset=RecipeIngredients.objects.filter(recipe=recipe), instance=recipe)
        allergens_formset = RecipeAllergensFormSet(prefix='allergens', instance=recipe)
        cooking_instructions_formset = RecipeCookingInstructionsFormSet(prefix='cooking_instructions', instance=recipe)

    return render(request, 'accounts/profile.html', {'form': form, 'formset': formset, 'allergens_formset': allergens_formset, 'cooking_instructions_formset': cooking_instructions_formset, 'recipe': recipe})
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SearchAllergensForm
import pandas as pd
from django.db.models import Q
from .utils import get_chart



# Functions used to return appropriate views/html template for the recipes app depending on the URL
def home(request):
    return render(request, "recipes/home.html")

class RecipeListViewUnsignedUsers(ListView):
    model = Recipe
    template_name = "recipes/unsigned_users_recipes.html"
    context_object_name = "recipes"

def make_recipe_name_clickable_unsigned_detail(row):
    recipe = Recipe.objects.get(pk=row['id'])
    recipe_url = recipe.get_absolute_url()
    difficulty = recipe.calculate_difficulty()
    return f'<a href="{recipe_url}">{row["recipe_name"]}</a> (Difficulty: {difficulty})'

def unsigned_user_redirect_recipes_list_page(request):
    form = SearchAllergensForm(request.POST or None)
    recipes_df = None
    chart = None

    if request.method == 'POST':
        if form.is_valid():
            allergens_input = request.POST.get('allergens')
            chart_type = request.POST.get('chart_type')
            print(allergens_input, chart_type)

            allergens_list = [allergen.strip() for allergen in allergens_input.split(',')]

            allergen_queries = Q()

            for allergen in allergens_list:
                allergen_query = Q(recipe_allergens__allergen__icontains=allergen)
                allergen_queries |= allergen_query

            qs = Recipe.objects.exclude(allergen_queries).values(
                'id', 'recipe_name', 'origin_country', 'cooking_time', 'recipe_category', 'recipe_estimated_cost')
            
            if qs:
                recipes_df = pd.DataFrame(qs)
                recipes_df['recipe_name'] = recipes_df.apply(make_recipe_name_clickable_unsigned_detail, axis=1)
                chart = get_chart(chart_type, recipes_df, labels=recipes_df['recipe_category'].values)
                recipes_df = recipes_df.to_html(escape=False)

    view = RecipeListViewUnsignedUsers()
    view.queryset = Recipe.objects.all()
    recipes = view.get_queryset()

    context = {
        'form': form,
        'object_list': recipes,
        'recipes_df': recipes_df,
        'chart': chart

    }
    return render(request, 'recipes/unsigned_users_recipes.html', context)

def make_recipe_name_clickable_signed_detail(row):
    recipe = Recipe.objects.get(pk=row['id'])
    recipe_url_signed_users = recipe.get_absolute_url_signed_users()
    difficulty = recipe.calculate_difficulty()
    return f'<a href="{recipe_url_signed_users}">{row["recipe_name"]}</a> (Difficulty: {difficulty})'

class RecipeListViewSignedUsers(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/signed_users_recipes.html"

@login_required
def signed_user_redirect_recipes_list_page(request):
    form = SearchAllergensForm(request.POST or None)
    recipes_df = None
    chart = None

    if request.method == 'POST':
        if form.is_valid():
            allergens_input = request.POST.get('allergens')
            chart_type = request.POST.get('chart_type')
            print(allergens_input, chart_type)

            allergens_list = [allergen.strip() for allergen in allergens_input.split(',')]

            allergen_queries = Q()

            for allergen in allergens_list:
                allergen_query = Q(recipe_allergens__allergen__icontains=allergen)
                allergen_queries |= allergen_query

            qs = Recipe.objects.exclude(allergen_queries).values(
                'id', 'recipe_name', 'origin_country', 'cooking_time', 'recipe_category', 'recipe_estimated_cost')
            
            if qs:
                recipes_df = pd.DataFrame(qs)
                recipes_df['recipe_name'] = recipes_df.apply(make_recipe_name_clickable_signed_detail, axis=1)
                chart = get_chart(chart_type, recipes_df, labels=recipes_df['recipe_category'].values)
                recipes_df = recipes_df.to_html(escape=False)


    view = RecipeListViewSignedUsers()
    view.queryset = Recipe.objects.all()
    recipes = view.get_queryset()

    context = {
        'form': form,
        'object_list': recipes,
        'recipes_df': recipes_df,
        'chart': chart

    }
    return render(request, 'recipes/signed_users_recipes.html', context)

class RecipeDetailViewUnsignedUsers(DetailView):
    model = Recipe
    template_name = "recipes/unsigned_users_recipes_details.html"

def unsigned_user_redirect_recipes_detailed_page(request, pk):
    view = RecipeDetailViewUnsignedUsers.as_view()
    return view(request, pk=pk)

class RecipeDetailViewSignedUsers(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/signed_users_recipes_details.html"

@login_required
def signed_user_redirect_recipes_detailed_page(request, pk):
    view = RecipeDetailViewSignedUsers.as_view()
    return view(request, pk=pk)



# Takes the request coming from the web app on recipes that are searched by name \
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_name(request):
    search_query = request.GET.get("query")
    matching_recipes = Recipe.objects.filter(recipe_name__icontains=search_query)

    recipes_json = [
        {
            "recipe_name": recipe.recipe_name,
            "recipe_origin_country": recipe.origin_country,
            "recipe_difficulty": recipe.difficulty,
            "recipe_category": recipe.recipe_category,
            "recipe_url": recipe.get_absolute_url(),
            "recipe_url_signed_users": recipe.get_absolute_url_signed_users(),
            "pic": recipe.pic.url,
        }
        for recipe in matching_recipes
    ]

    print(recipes_json)
    return JsonResponse({"recipes": recipes_json})


# Takes the request coming from the web app on recipes that are searched by filters \
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_filters(request):
    search_query1 = request.GET.get("query1")
    search_query2 = request.GET.get("query2")
    search_query3 = request.GET.get("query3")
    search_query4 = request.GET.get("query4")

    # Initialize the queryset with all recipes
    matching_recipes = Recipe.objects.all()

    if search_query1:
        matching_recipes = matching_recipes.filter(
            origin_country__icontains=search_query1
        )

    if search_query2:
        matching_recipes = matching_recipes.filter(
            recipe_category__icontains=search_query2
        )

    if search_query3:
        if search_query3 == "1":
            matching_recipes = matching_recipes.filter(cooking_time__lte=15)
        elif search_query3 == "2":
            matching_recipes = matching_recipes.filter(cooking_time__lte=30)
        elif search_query3 == "3":
            matching_recipes = matching_recipes.filter(cooking_time__lte=45)
        elif search_query3 == "4":
            matching_recipes = matching_recipes.filter(cooking_time__lte=60)
        elif search_query3 == "5":
            matching_recipes = matching_recipes.filter(cooking_time__gt=60)

    if search_query4:
        if search_query4 == "1":
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=5)
        elif search_query4 == "2":
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=10)
        elif search_query4 == "3":
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=20)
        elif search_query4 == "4":
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=30)
        elif search_query4 == "5":
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__gt=30)

    recipes_json = [
        {
            "recipe_name": recipe.recipe_name,
            "recipe_origin_country": recipe.origin_country,
            "recipe_difficulty": recipe.difficulty,
            "recipe_category": recipe.recipe_category,
            "recipe_url": recipe.get_absolute_url(),
            "recipe_url_signed_users": recipe.get_absolute_url_signed_users(),
            "pic": recipe.pic.url,
        }
        for recipe in matching_recipes
    ]

    return JsonResponse({"recipes": recipes_json})


# Takes the request coming from the web app on recipes that are searched by ingredients
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_ingredients(request):
    # Retrieves the 'query' parameter from the GET request
    search_query = request.GET.get("query")
    # Splits the search query (a comma-separated list of ingredients) into individual ingredients \
    # and stores them in a list called 'ingredients'. The strip() function is used to remove \
    # any leading or trailing whitespaces from each ingredient.
    ingredients = [ingredient.strip() for ingredient in search_query.split(",")]

    # Retrieves all recipes that contain the first ingredient in the ingredients list.
    matching_recipes = Recipe.objects.filter(
        recipe_ingredients__ingredient_name__icontains=ingredients[0]
    )

    # Code iterates over the remaining ingredients of the list (if any) using a for loop.
    # 'for ingredient in ingredients[1:]:' iterates over each ingredient in the list, skipping the \
    # first one.
    for ingredient in ingredients[1:]:
        # For each ingredient in the loop, it further filters the recipes to find those containing \
        # the current ingredient.
        matching_recipes = matching_recipes.filter(
            recipe_ingredients__ingredient_name__icontains=ingredient
        )

    recipes_json = [
        {
            "recipe_name": recipe.recipe_name,
            "recipe_origin_country": recipe.origin_country,
            "recipe_difficulty": recipe.difficulty,
            "recipe_category": recipe.recipe_category,
            "recipe_url": recipe.get_absolute_url(),
            "recipe_url_signed_users": recipe.get_absolute_url_signed_users(),
            "pic": recipe.pic.url,
        }
        for recipe in matching_recipes
    ]

    return JsonResponse({"recipes": recipes_json})

# Logic to allow users to add comments to recipes
def publish_comment(request, pk):
    if request.method == 'POST':
        comment_text = request.POST.get('comment') 
        recipe = Recipe.objects.get(pk=pk)
        recipe.comments.create(text=comment_text, user=request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
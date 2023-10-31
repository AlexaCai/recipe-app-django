from django.shortcuts import render
from django.views.generic import ListView     
from .models import Recipe
from django.http import JsonResponse

# Takes the request coming from the web app and returns the template available at \
# recipes/home.html as a response.
def home(request):
   return render(request, 'recipes/home.html')

# Takes the request coming from the web app on recipes that are searched by name \
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_name(request):
    search_query = request.GET.get('query')
    matching_recipes = Recipe.objects.filter(recipe_name__icontains=search_query)

    recipes_json = [{'recipe_name': recipe.recipe_name, 'recipe_origin_country': recipe.origin_country, 'recipe_difficulty': recipe.difficulty, 'recipe_category': recipe.recipe_category, 'pic': recipe.pic.url} for recipe in matching_recipes]
    print(recipes_json)
    return JsonResponse({'recipes': recipes_json})

# Takes the request coming from the web app on recipes that are searched by filters \
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_filters(request):
    search_query1 = request.GET.get('query1')
    search_query2 = request.GET.get('query2')
    search_query3 = request.GET.get('query3')
    search_query4 = request.GET.get('query4')

    # Initialize the queryset with all recipes
    matching_recipes = Recipe.objects.all()

    if search_query1:
        matching_recipes = matching_recipes.filter(origin_country__icontains=search_query1)

    if search_query2:
        matching_recipes = matching_recipes.filter(recipe_category__icontains=search_query2)

    if search_query3:
        if search_query3 == '1':
            matching_recipes = matching_recipes.filter(cooking_time__lte=15)
        elif search_query3 == '2':
            matching_recipes = matching_recipes.filter(cooking_time__lte=30)
        elif search_query3 == '3':
            matching_recipes = matching_recipes.filter(cooking_time__lte=45)
        elif search_query3 == '4':
            matching_recipes = matching_recipes.filter(cooking_time__lte=60)
        elif search_query3 == '5':
            matching_recipes = matching_recipes.filter(cooking_time__gt=60)

    if search_query4:
        if search_query4 == '1':
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=5)
        elif search_query4 == '2':
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=10)
        elif search_query4 == '3':
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=20)
        elif search_query4 == '4':
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__lte=30)
        elif search_query4 == '5':
            matching_recipes = matching_recipes.filter(recipe_estimated_cost__gt=30)

    recipes_json = [
        {
            'recipe_name': recipe.recipe_name,
            'recipe_origin_country': recipe.origin_country,
            'recipe_difficulty': recipe.difficulty,
            'recipe_category': recipe.recipe_category,
            'pic': recipe.pic.url
        }
        for recipe in matching_recipes
    ]

    return JsonResponse({'recipes': recipes_json})

# Takes the request coming from the web app on recipes that are searched by name \
# and returns the JSON response containing the recipes that match the search query.
def search_recipes_by_ingredients(request):
    search_query = request.GET.get('query')
    matching_recipes = Recipe.objects.filter(ingredient_name__icontains=search_query)

    recipes_json = [{'recipe_name': recipe.recipe_name, 'recipe_origin_country': recipe.origin_country, 'recipe_difficulty': recipe.difficulty, 'recipe_category': recipe.recipe_category, 'pic': recipe.pic.url} for recipe in matching_recipes]
    print(recipes_json)
    return JsonResponse({'recipes': recipes_json})

class RecipeListView(ListView):                             
   model = Recipe                                           
   template_name = 'recipes/unsigned_users_recipes.html'    

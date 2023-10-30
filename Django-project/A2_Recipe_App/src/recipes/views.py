from django.shortcuts import render
from django.views.generic import ListView     
from .models import Recipe
from django.http import JsonResponse

# Takes the request coming from the web application and returns the template available at \
# recipes/recipes_home.html as a response.
def home(request):
   return render(request, 'recipes/home.html')

def search_recipes(request):
    search_query = request.GET.get('query')
    matching_recipes = Recipe.objects.filter(recipe_name__icontains=search_query)

    recipes_json = [{'recipe_name': recipe.recipe_name, 'recipe_origin_country': recipe.origin_country, 'recipe_difficulty': recipe.difficulty, 'recipe_category': recipe.recipe_category, 'pic': recipe.pic.url} for recipe in matching_recipes]
    print(recipes_json)
    return JsonResponse({'recipes': recipes_json})

class RecipeListView(ListView):                             
   model = Recipe                                           
   template_name = 'recipes/unsigned_users_recipes.html'    

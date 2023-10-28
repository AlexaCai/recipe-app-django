from django.shortcuts import render
from django.views.generic import ListView      #to display lists
from .models import Recipe                     #to access Book model

# Create your views here.

# Takes the request coming from the web application and returns the template available at \
# recipes/recipes_home.html as a response.
def home(request):
   return render(request, 'recipes/home.html')

class RecipeListView(ListView):                             #class-based view
   model = Recipe                                           #specify model
   template_name = 'recipes/unsigned_users_recipes.html'    #specify template 

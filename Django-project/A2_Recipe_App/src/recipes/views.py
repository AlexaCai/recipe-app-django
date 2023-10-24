from django.shortcuts import render

# Create your views here.

# Takes the request coming from the web application and returns the template available at \
# recipes/recipes_home.html as a response.
def home(request):
   return render(request, 'recipes/recipes_home.html')
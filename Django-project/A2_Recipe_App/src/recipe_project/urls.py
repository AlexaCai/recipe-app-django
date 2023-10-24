"""
URL configuration for recipe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include


# The empty quotes '' indicate that this path refers to the home page 'http://127.0.0.1:8000/' and \
# include('recipes.urls') will link the URL with the app and view information available at \ 
# 'recipes.urls' (the 'recipes/urls.py' file). 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

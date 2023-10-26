from django.contrib import admin
from .models import Recipe, RecipeIngredients  # Import the RecipeIngredients model

# Define an inline formset for the RecipeIngredients model
from django.forms import inlineformset_factory

class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time', 'origin_country', 'creation_date')
    inlines = [RecipeIngredientsInline]

admin.site.register(Recipe, RecipeAdmin)

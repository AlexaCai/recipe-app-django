from django import forms    #import django forms
from recipes.models import Recipe

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

#define class-based Form imported from Django forms
class SearchAllergensForm(forms.Form): 
   allergens = forms.CharField(        
        label="Allergen(s)",
        max_length=120,
        required=False
        )
   
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class UserSubmitRecipe(forms.ModelForm):
    recipe_name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    special_note = forms.CharField(widget=forms.Textarea, required=False)
    cooking_time = forms.IntegerField(required=True)
    number_of_portions = forms.IntegerField(required=True)
    recipe_estimated_cost = forms.DecimalField(required=True, max_digits=5, decimal_places=2)

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'cooking_time', 'description', 'special_note', 'number_of_portions', 'recipe_estimated_cost', 'origin_country', 'recipe_category', 'pic']

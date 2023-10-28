from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

unit_measure_choices = (
    ("ml - milliliter", "ml - Milliliter"),
    ("fl oz - fluid ounce", "fl oz - Fluid Ounce"),
    ("tbsp - tablespoon", "tbsp - Tablespoon"),
    ("tsp - teaspoon", "tsp - Teaspoon"),
    ("L - liter", "L - Liter"),
    ("pt - pint", "pt - Pint"),
    ("g - gram", "g - Gram"),
    ("oz - ounce", "oz - Ounce"),
    ("lb - pound", "lb - Pound"),
    ("kg - kilogram", "kg - Kilogram"),
    ("unit", "Unit"),
    ("units", "Units"),
)

country_choices = (
    ("afghan", "Afghan"),
    ("albanian", "Albanian "),
    ("algerian", "Algerian"),
    ("american", "American"),
    ("andorran", "Andorran"),
    ("angolan", "Angolan"),
    ("argentine", "Argentine"),
    ("armenian", "Armenian"),
    ("australian", "Australian"),
    ("austrian", "Austrian"),
    ("azerbaijani", "Azerbaijani"),
    ("bahamian", "Bahamian"),
    ("bahraini", "Bahraini"),
    ("bangladeshi", "Bangladeshi"),
    ("barbadian", "Barbadian"),
    ("belarusian", "Belarusian"),
    ("belgian", "Belgian"),
    ("belizean", "Belizean"),
    ("beninese", "Beninese"),
    ("bhutanese", "Bhutanese"),
    ("bolivian", "Bolivian"),
    ("bosnian", "Bosnian"),
    ("brazilian", "Brazilian"),
    ("british", "British"),
    ("bruneian", "Bruneian"),
    ("bulgarian", "Bulgarian"),
    ("burkinabe", "Burkinabe"),
    ("burundian", "Burundian"),
    ("cambodian", "Cambodian"),
    ("cameroonian", "Cameroonian"),
    ("canadian", "Canadian"),
    ("cape verdean", "Cape Verdean"),
    ("central african", "Central African"),
    ("chadian", "Chadian"),
    ("chilean", "Chilean"),
    ("chinese", "Chinese"),
    ("colombian", "Colombian"),
    ("comoran", "Comoran"),
    ("congolese", "Congolese"),
    ("costa rican", "Costa Rican"),
    ("croatian", "Croatian"),
    ("cuban", "Cuban"),
    ("cyprio", "Cyprio"),
    ("czech", "Czech"),
    ("danish", "Danish"),
    ("djiboutian", "Djiboutian"),
    ("dominican", "Dominican"),
    ("dominican republic", "Dominican Republic"),
    ("dutch", "Dutch"),
    ("east timorese", "East Timorese"),
    ("ecuadorian", "Ecuadorian"),
    ("egyptian", "Egyptian"),
    ("emirati", "Emirati"),
    ("eritrean", "Eritrean"),
    ("estonian", "Estonian"),
    ("ethiopian", "Ethiopian"),
    ("fijian", "Fijian"),
    ("filipino", "Filipino"),
    ("finnish", "Finnish"),
    ("french", "French"),
    ("gabonese", "Gabonese"),
    ("gambian", "Gambian"),
    ("georgian", "Georgian"),
    ("german", "German"),
    ("ghanaian", "Ghanaian"),
    ("greek", "Greek"),
    ("grenadian", "Grenadian"),
    ("guatemalan", "Guatemalan"),
    ("guinean", "Guinean"),
    ("guyanese", "Guyanese"),
    ("haitian", "Haitian"),
    ("honduran", "Honduran"),
    ("hungarian", "Hungarian"),
    ("icelandic", "Icelandic"),
    ("indian", "Indian"),
    ("indonesian", "Indonesian"),
    ("iranian", "Iranian"),
    ("iraqi", "Iraqi"),
    ("irish", "Irish"),
    ("israeli", "Israeli"),
    ("italian", "Italian"),
    ("ivorian", "Ivorian"),
    ("jamaican", "Jamaican"),
    ("japanese", "Japanese"),
    ("jordanian", "Jordanian"),
    ("kazakhstani", "Kazakhstani"),
    ("kenyan", "Kenyan"),
    ("kuwaiti", "Kuwaiti"),
    ("kyrgyz", "Kyrgyz"),
    ("laotian", "Laotian"),
    ("latvian", "Latvian"),
    ("lebanese", "Lebanese"),
    ("lesotho", "Lesotho"),
    ("liberian", "Liberian"),
    ("libyan", "Libyan"),
    ("liechtensteiner", "Liechtensteiner"),
    ("lithuanian", "Lithuanian"),
    ("luxembourgish", "Luxembourgish"),
    ("macedonian", "Macedonian"),
    ("malagasy", "Malagasy"),
    ("malawian", "Malawian"),
    ("malaysian", "Malaysian"),
    ("maldivian", "Maldivian"),
    ("malian", "Malian"),
    ("maltese", "Maltese"),
    ("mauritanian", "Mauritanian"),
    ("mauritian", "Mauritian"),
    ("mexican", "Mexican"),
    ("moldovan", "Moldovan"),
    ("monegasque", "Monegasque"),
    ("mongolian", "Mongolian"),
    ("montenegrin", "Montenegrin"),
    ("moroccan", "Moroccan"),
    ("mozambican", "Mozambican"),
    ("namibian", "Namibian"),
    ("nepalese", "Nepalese"),
    ("new zealand", "New Zealand"),
    ("nicaraguan", "Nicaraguan"),
    ("nigerian", "Nigerian"),
    ("north korean", "North Korean"),
    ("norwegian", "Norwegian"),
    ("omani", "Omani"),
    ("pakistani", "Pakistani"),
    ("palauan", "Palauan"),
    ("palestinian", "Palestinian"),
    ("panamanian", "Panamanian"),
    ("papua new guinean", "Papua New Guinean"),
    ("paraguayan", "Paraguayan"),
    ("peruvian", "Peruvian"),
    ("polish", "Polish"),
    ("portuguese", "Portuguese"),
    ("qatari", "Qatari"),
    ("romanian", "Romanian"),
    ("russian", "Russian"),
    ("rwandan", "Rwandan"),
    ("saint kitts and nevis", "Saint Kitts and Nevis"),
    ("saint lucian", "Saint Lucian"),
    ("saint vincent and the grenadines", "Saint Vincent and the Grenadines"),
    ("salvadoran", "Salvadoran"),
    ("sammarinese", "Sammarinese"),
    ("sao tomean", "Sao Tomean"),
    ("saudi arabian", "Saudi Arabian"),
    ("senegalese", "Senegalese"),
    ("serbian", "Serbian"),
    ("seychellois", "Seychellois"),
    ("sierra leonean", "Sierra Leonean"),
    ("singaporean", "Singaporean"),
    ("slovak", "Slovak"),
    ("slovenian", "Slovenian"),
    ("solomon islands", "Solomon Islands"),
    ("somali", "Somali"),
    ("south african", "South African"),
    ("south korean", "South Korean"),
    ("south sudanese", "South Sudanese"),
    ("spanish", "Spanish"),
    ("sri lankan", "Sri Lankan"),
    ("sudanese", "Sudanese"),
    ("surinamese", "Surinamese"),
    ("swazi", "Swazi"),
    ("swedish", "Swedish"),
    ("swiss", "Swiss"),
    ("syrian", "Syrian"),
    ("tajik", "Tajik"),
    ("tanzanian", "Tanzanian"),
    ("thai", "Thai"),
    ("togolese", "Togolese"),
    ("tongan", "Tongan"),
    ("trinidadian and tobagonian", "Trinidadian and Tobagonian"),
    ("tunisian", "Tunisian"),
    ("turkish", "Turkish"),
    ("turkmen", "Turkmen"),
    ("tuvaluan", "Tuvaluan"),
    ("ugandan", "Ugandan"),
    ("ukrainian", "Ukrainian"),
    ("uruguayan", "Uruguayan"),
    ("uzbek", "Uzbek"),
    ("vanuatuan", "Vanuatuan"),
    ("venezuelan", "Venezuelan"),
    ("vietnamese", "Vietnamese"),
    ("yemeni", "Yemeni"),
    ("zambian", "Zambian"),
    ("zimbabwean", "Zimbabwean"),
    ("other", "Other"),
    ("no category", "No Category"),
)

category_choices = (
    ("appetizer", "Appetizer"),
    ("baked", "Baked"),
    ("breakfast", "Breakfast"),
    ("brunch", "Brunch"),
    ("cafe/tea", "Cafe/Tea"),
    ("condiment", "Condiment"),
    ("dinner", "Dinner"),
    ("dessert", "Dessert"),
    ("drink/cocktail", "Drink/Cocktail"),
    ("fish", "Fish"),
    ("fruit", "Fruit"),
    ("holiday", "Holiday"),
    ("hot beverage", "Hot beverages"),
    ("juice", "Juice"),
    ("lunch", "Lunch"),
    ("meat", "Meat"),
    ("pasta", "Pasta"),
    ("salad", "Salad"),
    ("sandwhich", "Sandwhich"),
    ("sauce", "Sauce"),
    ("seafood", "Seafood"),
    ("side", "Side"),
    ("smoothie/shake", "Smoothie/Shake"),
    ("snack", "Snack"),
    ("soup", "Soup"),
    ("vegan", "Vegan"),
    ("vegetable", "Vegetable"),
    ("vegetarian", "Vegetarian"),
)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    creator_name = models.CharField(max_length=50, blank=True, help_text="This field is optional")
    description = models.TextField(blank=True, help_text="This field is optional")
    special_note = models.TextField(blank=True, help_text="This field is optional")
    cooking_time = models.IntegerField(help_text="Indicates in minutes")
    number_of_portions = models.IntegerField(default=4, help_text="Indicates how many servings this recipe is for")
    recipe_estimated_cost = models.FloatField(default=10, help_text="Estimated total cost in dollar $")
    cooking_instructions = models.TextField()
    origin_country = models.CharField(max_length=30, choices=country_choices, default="other", help_text="Select the country associated to this recipe",)
    recipe_category = models.CharField(max_length=100, choices=category_choices, default="other", help_text="Select the category associated to this recipe",)
    allergens = models.CharField(max_length=100, default="None", help_text="Indicate all allergens contained in this recipe",)
    creation_date = models.DateField(auto_now_add=True)
    pic = models.ImageField(upload_to="recipes", default="no_picture.jpg")

    def calculate_difficulty(self):
        ingredient_count = self.recipe_ingredients.count()
        if self.cooking_time < 10 and ingredient_count < 4:
            return "easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            return "medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            return "intermediate"
        elif self.cooking_time >= 10 and ingredient_count >= 4:
            return "hard"

    # Display the difficulty as a property, not an input field
    @property
    def difficulty(self):
        return self.calculate_difficulty()

    # Generates a URL for a recipe instance created
    def generate_url(self):
        if self.id:
            return f"http://127.0.0.1:8000/admin/recipes/recipe/{self.id}"
        else:
            return ""
        
    # Display the url as a property, not an input field
    @property
    def recipe_url(self):
        return self.generate_url()

    def __str__(self):
        return self.recipe_name
    
# Ensure users can enter ingredient along with quantity and unit of measure, one by one
class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient_name = models.CharField(max_length=100)
    quantity = models.FloatField(default="")
    unit_of_measurement = models.CharField(max_length=20, choices=unit_measure_choices)
    possible_substitute = models.CharField(max_length=100, blank=True, help_text="Optional - Indicate here which ingredient could replace the one mentionned if not available")
    substitue_special_note = models.CharField(max_length=300, blank=True, help_text="This field is optional")

    # Used to ensure that the name of this section in Django admin interface is written without an 's'
    class Meta:
        verbose_name = "Recipe ingredient"
        verbose_name_plural = "Recipe Ingredient"

# Ensure users can enter cooking instructions for the recipe, one by one
class RecipeCookingInstructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_instructions")
    step_name = models.CharField(max_length=100)
    step_instruction = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Recipe cooking instruction"
        verbose_name_plural = "Recipe cooking instruction"

# Ensure users can enter cooking tools needed for the recipe, one by one
class RecipeToolsNeeded(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_tools")
    cooking_tool_name = models.CharField(max_length=100)
    cooking_tool_pic = models.ImageField(upload_to="cooking_tools", default="no_picture.jpg")


    class Meta:
        verbose_name = "Recipe required tool"
        verbose_name_plural = "Recipe required tool"

# Allow user to add similar recipes when creating a recipe
class RecipeSimilarComplementary(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_complementary")
    complementary_recipe_name = models.CharField(max_length=100, blank=True)
    complementary_recipe_link = models.URLField(max_length=500, blank=True)
    similar_recipe_pic = models.ImageField(upload_to="recipes", default="no_picture.jpg")

    def clean(self):
        super().clean()

        if self.complementary_recipe_name:
            # If complementary_recipe_name has a value, complementary_recipe_link must also have a value
            if not self.complementary_recipe_link:
                raise ValidationError({"complementary_recipe_link": "Complementary recipe link is required if complementary recipe name is provided."})
        else:
            # If complementary_recipe_name is empty, complementary_recipe_link should also be empty
            if self.complementary_recipe_link:
                raise ValidationError({"complementary_recipe_name": "Complementary recipe name must be provided if a complementary recipe link is provided."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Similar/complementary recipe"
        verbose_name_plural = "Similar/complementary recipe"


# Model used to allow users to comment recipes
class RecipeComments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Recipe comment(s)"
        verbose_name_plural = "Recipe comment(s)"

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe.recipe_name}"

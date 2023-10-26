from django.db import models

# Create your models here.

unit_measure_choices= (
('ml - milliliter', 'ml - Milliliter'), 
('fl oz - fluid ounce', 'fl oz - Fluid Ounce'), 
('tbsp - tablespoon', 'tbsp - Tablespoon'), 
('tsp - teaspoon', 'tsp - Teaspoon'), 
('L - liter', 'L - Liter'), 
('pt - pint', 'pt - Pint'), 
('g - gram', 'g - Gram'), 
('oz - ounce', 'oz - Ounce'), 
('lb - pound', 'lb - Pound'), 
('kg - kilogram', 'kg - Kilogram'), 
('unit', 'Unit'),
('units', 'Units'), 
)

category_choices= (
('afghan', 'Afghan'), 
('albanian', 'Albanian '), 
('algerian', 'Algerian'), 
('american', 'American'), 
('andorran', 'Andorran'), 
('angolan', 'Angolan'),
('argentine', 'Argentine'),
('armenian', 'Armenian'),
('australian', 'Australian'),
('austrian', 'Austrian'),
('azerbaijani', 'Azerbaijani'),
('bahamian', 'Bahamian'),
('bahraini', 'Bahraini'),
('bangladeshi', 'Bangladeshi'),
('barbadian', 'Barbadian'),
('belarusian', 'Belarusian'),
('belgian', 'Belgian'),
('belizean', 'Belizean'),
('beninese', 'Beninese'),
('bhutanese', 'Bhutanese'),
('bolivian', 'Bolivian'),
('bosnian', 'Bosnian'),
('brazilian', 'Brazilian'),
('british', 'British'),
('bruneian', 'Bruneian'),
('bulgarian', 'Bulgarian'),
('burkinabe', 'Burkinabe'),
('burundian', 'Burundian'),
('cambodian', 'Cambodian'),
('cameroonian', 'Cameroonian'),
('canadian', 'Canadian'),
('cape verdean', 'Cape Verdean'),
('central african', 'Central African'),
('chadian', 'Chadian'),
('chilean', 'Chilean'),
('chinese', 'Chinese'),
('colombian', 'Colombian'),
('comoran', 'Comoran'),
('congolese', 'Congolese'),
('costa rican', 'Costa Rican'),
('croatian', 'Croatian'),
('cuban', 'Cuban'),
('cyprio', 'Cyprio'),
('czech', 'Czech'),
('danish', 'Danish'),
('djiboutian', 'Djiboutian'),
('dominican', 'Dominican'),
('dutch', 'Dutch'),
('east timorese', 'East Timorese'),
('ecuadorian', 'Ecuadorian'),
('egyptian', 'Egyptian'),
('emirati', 'Emirati'),
('eritrean', 'Eritrean'),
('estonian', 'Estonian'),
('ethiopian', 'Ethiopian'),
('fijian', 'Fijian'),
('filipino', 'Filipino'),
('finnish', 'Finnish'),
('french', 'French'),
('gabonese', 'Gabonese'),
('gambian', 'Gambian'),
('georgian', 'Georgian'),
('german', 'German'),
('ghanaian', 'Ghanaian'),
('greek', 'Greek'),
('grenadian', 'Grenadian'),
('guatemalan', 'Guatemalan'),
('guinean', 'Guinean'),
('guyanese', 'Guyanese'),
('haitian', 'Haitian'),
('honduran', 'Honduran'),
('hungarian', 'Hungarian'),
('icelandic', 'Icelandic'),
('indian', 'Indian'),
('indonesian', 'Indonesian'),
('iranian', 'Iranian'),
('iraqi', 'Iraqi'),
('irish', 'Irish'),
('israeli', 'Israeli'),
('italian', 'Italian'),
('ivorian', 'Ivorian'),
('jamaican', 'Jamaican'),
('japanese', 'Japanese'),
('jordanian', 'Jordanian'),
('kazakhstani', 'Kazakhstani'),
('kenyan', 'Kenyan'),
('kuwaiti', 'Kuwaiti'),
('kyrgyz', 'Kyrgyz'),
('laotian', 'Laotian'),
('latvian', 'Latvian'),
('lebanese', 'Lebanese'),
('lesotho', 'Lesotho'),
('liberian', 'Liberian'),
('libyan', 'Libyan'),
('liechtensteiner', 'Liechtensteiner'),
('lithuanian', 'Lithuanian'),
('luxembourgish', 'Luxembourgish'),
('macedonian', 'Macedonian'),
('malagasy', 'Malagasy'),
('malawian', 'Malawian'),
('malaysian', 'Malaysian'),
('maldivian', 'Maldivian'),
('malian', 'Malian'),
('maltese', 'Maltese'),
('mauritanian', 'Mauritanian'),
('mauritian', 'Mauritian'),
('mexican', 'Mexican'),
('moldovan', 'Moldovan'),
('monegasque', 'Monegasque'),
('mongolian', 'Mongolian'),
('montenegrin', 'Montenegrin'),
('moroccan', 'Moroccan'),
('mozambican', 'Mozambican'),
('namibian', 'Namibian'),
('nepalese', 'Nepalese'),
('new zealand', 'New Zealand'),
('nicaraguan', 'Nicaraguan'),
('nigerian', 'Nigerian'),
('north korean', 'North Korean'),
('norwegian', 'Norwegian'),
('omani', 'Omani'),
('pakistani', 'Pakistani'),
('palauan', 'Palauan'),
('palestinian', 'Palestinian'),
('panamanian', 'Panamanian'),
('papua new guinean', 'Papua New Guinean'),
('paraguayan', 'Paraguayan'),
('peruvian', 'Peruvian'),
('polish', 'Polish'),
('portuguese', 'Portuguese'),
('qatari', 'Qatari'),
('romanian', 'Romanian'),
('russian', 'Russian'),
('rwandan', 'Rwandan'),
('saint kitts and nevis', 'Saint Kitts and Nevis'),
('saint lucian', 'Saint Lucian'),
('salvadoran', 'Salvadoran'),
('sammarinese', 'Sammarinese'),
('sao tomean', 'Sao Tomean'),
('saudi arabian', 'Saudi Arabian'),
('senegalese', 'Senegalese'),
('serbian', 'Serbian'),
('seychellois', 'Seychellois'),
('sierra leonean', 'Sierra Leonean'),
('singaporean', 'Singaporean'),
('slovak', 'Slovak'),
('slovenian', 'Slovenian'),
('solomon islands', 'Solomon Islands'),
('somali', 'Somali'),
('south african', 'South African'),
('south korean', 'South Korean'),
('south sudanese', 'South Sudanese'),
('spanish', 'Spanish'),
('sri lankan', 'Sri Lankan'),
('sudanese', 'Sudanese'),
('surinamese', 'Surinamese'),
('swazi', 'Swazi'),
('swedish', 'Swedish'),
('swiss', 'Swiss'),
('syrian', 'Syrian'),
('tajik', 'Tajik'),
('tanzanian', 'Tanzanian'),
('thai', 'Thai'),
('togolese', 'Togolese'),
('tongan', 'Tongan'),
('trinidadian and tobagonian', 'Trinidadian and Tobagonian'),
('tunisian', 'Tunisian'),
('turkish', 'Turkish'),
('turkmen', 'Turkmen'),
('tuvaluan', 'Tuvaluan'),
('ugandan', 'Ugandan'),
('ukrainian', 'Ukrainian'),
('uruguayan', 'Uruguayan'),
('uzbek', 'Uzbek'),
('vanuatuan', 'Vanuatuan'),
('venezuelan', 'Venezuelan'),
('vietnamese', 'Vietnamese'),
('yemeni', 'Yemeni'),
('zambian', 'Zambian'),
('zimbabwean', 'Zimbabwean'),
('other', 'Other'),
('no category', 'No Category'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=50) 
    description = models.TextField(blank=True) 
    cooking_time = models.IntegerField(help_text= 'in minutes') 
    difficulty = models.CharField(max_length=20, blank=True, null=True, help_text='This value is calculated automatically, not input require here.')  # New field to store difficulty
    cooking_instructions = models.TextField() 
    origin_country = models.CharField(max_length=30, choices=category_choices, default='other', help_text= 'select the country associated to the recipe') # ok 
    creation_date = models.DateField(auto_now_add=True) 
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')



    def save(self, *args, **kwargs):
        super(Recipe, self).save(*args, **kwargs)
        self.difficulty = self.calculate_difficulty()
        super(Recipe, self).save(update_fields=['difficulty'])

    def calculate_difficulty(self):
        # Count the number of related RecipeIngredients objects for this recipe
        ingredient_count = self.recipe_ingredients.count()
        if self.cooking_time < 10 and ingredient_count < 4:
            return "easy"
        elif self.cooking_time < 10 and ingredient_count >= 4:
            return "medium"
        elif self.cooking_time >= 10 and ingredient_count < 4:
            return "intermediate"
        elif self.cooking_time >= 10 and ingredient_count >= 4:
            return "hard"
    
    def __str__(self):
        return self.name
    
class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')  # Specify a custom related_name
    ingredient_name = models.CharField(max_length=100)
    quantity = models.FloatField(default='')
    unit_of_measurement = models.CharField(max_length=20, choices=unit_measure_choices)


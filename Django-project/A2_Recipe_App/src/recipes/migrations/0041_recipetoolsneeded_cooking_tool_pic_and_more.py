# Generated by Django 4.2.6 on 2023-10-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0040_remove_recipe_recipe_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipetoolsneeded',
            name='cooking_tool_pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='cooking_tools'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_category',
            field=models.CharField(choices=[('appetizer', 'Appetizer'), ('baked', 'Baked'), ('breakfast', 'Breakfast'), ('brunch', 'Brunch'), ('cafe/tea', 'Cafe/Tea'), ('condiment', 'Condiment'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('drink/cocktail', 'Drink/Cocktail'), ('fish', 'Fish'), ('fruit', 'Fruit'), ('holiday', 'Holiday'), ('hot beverage', 'Hot beverages'), ('juice', 'Juice'), ('lunch', 'Lunch'), ('meat', 'Meat'), ('pasta', 'Pasta'), ('salad', 'Salad'), ('sandwhich', 'Sandwhich'), ('sauce', 'Sauce'), ('seafood', 'Seafood'), ('side', 'Side'), ('smoothie/shake', 'Smoothie/Shake'), ('snack', 'Snack'), ('soup', 'Soup'), ('vegan', 'Vegan'), ('vegetable', 'Vegetable'), ('vegetarian', 'Vegetarian')], default='other', help_text='Select the category associated to this recipe', max_length=30),
        ),
    ]

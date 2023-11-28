# Generated by Django 4.2.6 on 2023-11-27 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0054_recipecomments_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredients',
            name='unit_of_measurement',
            field=models.CharField(choices=[('ml - milliliter', 'ml - Milliliter'), ('fl oz - fluid ounce', 'fl oz - Fluid Ounce'), ('tbsp - tablespoon', 'tbsp - Tablespoon'), ('tsp - teaspoon', 'tsp - Teaspoon'), ('L - liter', 'L - Liter'), ('pt - pint', 'pt - Pint'), ('g - gram', 'g - Gram'), ('oz - ounce', 'oz - Ounce'), ('lb - pound', 'lb - Pound'), ('kg - kilogram', 'kg - Kilogram'), ('unit', 'Unit'), ('units', 'Units')], default='ml - milliliter', max_length=20),
        ),
    ]
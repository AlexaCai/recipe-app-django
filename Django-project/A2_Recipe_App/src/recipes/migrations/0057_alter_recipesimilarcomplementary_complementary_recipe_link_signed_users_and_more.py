# Generated by Django 4.2.6 on 2023-11-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0056_alter_recipeingredients_unit_of_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesimilarcomplementary',
            name='complementary_recipe_link_signed_users',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='recipesimilarcomplementary',
            name='complementary_recipe_link_unsigned_users',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
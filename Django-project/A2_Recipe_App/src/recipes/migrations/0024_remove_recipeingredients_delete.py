# Generated by Django 4.2.6 on 2023-10-26 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_recipeingredients_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredients',
            name='delete',
        ),
    ]

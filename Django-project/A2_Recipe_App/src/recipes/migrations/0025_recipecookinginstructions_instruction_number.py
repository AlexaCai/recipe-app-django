# Generated by Django 4.2.6 on 2023-10-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_remove_recipeingredients_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipecookinginstructions',
            name='instruction_number',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]

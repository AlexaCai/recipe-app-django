# Generated by Django 4.2.6 on 2023-10-26 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_recipe_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='pic',
            new_name='picture',
        ),
    ]

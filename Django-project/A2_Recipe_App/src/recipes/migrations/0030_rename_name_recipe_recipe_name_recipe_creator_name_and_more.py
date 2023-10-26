# Generated by Django 4.2.6 on 2023-10-26 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0029_alter_recipecookinginstructions_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='recipe_name',
        ),
        migrations.AddField(
            model_name='recipe',
            name='creator_name',
            field=models.CharField(blank=True, help_text='This field is optional', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(help_text='Indicates in minutes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, help_text='This field is optional'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='special_note',
            field=models.TextField(blank=True, help_text='This field is optional'),
        ),
        migrations.CreateModel(
            name='RecipeSimilarComplementary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complementary_recipe_name', models.CharField(blank=True, max_length=100)),
                ('complementary_recipe_link', models.CharField(blank=True, max_length=500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_complementary', to='recipes.recipe')),
            ],
            options={
                'verbose_name': 'Recipe required tool',
                'verbose_name_plural': 'Recipe required tool',
            },
        ),
    ]

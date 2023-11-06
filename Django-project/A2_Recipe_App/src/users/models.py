from django.db import models
from recipes.models import Recipe

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    favorite_recipes = models.ManyToManyField(Recipe, related_name='users_favorite_recipes', blank=True)
    notes = models.TextField(blank=True)
    pic = models.ImageField(upload_to='users', default='no_picture.jpg')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
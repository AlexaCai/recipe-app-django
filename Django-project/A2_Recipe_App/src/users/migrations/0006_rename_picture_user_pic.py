# Generated by Django 4.2.6 on 2023-10-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='picture',
            new_name='pic',
        ),
    ]

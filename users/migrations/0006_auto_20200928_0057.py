# Generated by Django 3.0.8 on 2020-09-27 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='Movie_name',
            new_name='movie_name',
        ),
    ]
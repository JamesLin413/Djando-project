# Generated by Django 4.0.6 on 2022-07-28 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_food_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['-price']},
        ),
    ]

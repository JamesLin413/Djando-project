# Generated by Django 4.0.6 on 2022-07-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0013_subway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description '),
        ),
    ]

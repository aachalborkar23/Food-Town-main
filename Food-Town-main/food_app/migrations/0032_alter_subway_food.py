# Generated by Django 4.2.6 on 2023-10-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0031_alter_subway_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='food',
            field=models.IntegerField(choices=[(1, 'Veg'), (2, 'Non Veg')], max_length=50, verbose_name='Food '),
        ),
    ]

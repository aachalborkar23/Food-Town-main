# Generated by Django 4.2.6 on 2023-11-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0040_alter_toprestaurant_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toprestaurant',
            name='variety',
            field=models.CharField(max_length=30, verbose_name='variety'),
        ),
    ]
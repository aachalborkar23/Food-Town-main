# Generated by Django 4.2.6 on 2023-10-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0014_alter_subway_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menus1',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-29 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0023_alter_menufilter_menuid_alter_menufilter_resid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menufilter',
            name='menuid',
            field=models.ForeignKey(db_column='menuid', on_delete=django.db.models.deletion.CASCADE, to='food_app.menus1'),
        ),
    ]

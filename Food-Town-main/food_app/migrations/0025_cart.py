# Generated by Django 4.2.6 on 2023-10-30 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0024_alter_menufilter_menuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dominoid', models.ForeignKey(db_column='Dominoid', on_delete=django.db.models.deletion.CASCADE, to='food_app.dominopizza')),
                ('Subwayid', models.ForeignKey(db_column='Subwayid', on_delete=django.db.models.deletion.CASCADE, to='food_app.subway')),
                ('resid', models.ForeignKey(db_column='resid', on_delete=django.db.models.deletion.CASCADE, to='food_app.toprestaurant')),
                ('uid', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('upass', models.CharField(max_length=50)),
                ('ucpass', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

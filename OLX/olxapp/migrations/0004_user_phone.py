# Generated by Django 5.0.6 on 2024-05-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxapp', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.0.6 on 2023-02-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rate_listing',
            field=models.CharField(default='', max_length=200),
        ),
    ]
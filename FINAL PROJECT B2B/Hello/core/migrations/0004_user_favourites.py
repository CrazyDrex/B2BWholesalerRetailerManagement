# Generated by Django 4.0.6 on 2023-02-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.CharField(default='', max_length=200),
        ),
    ]

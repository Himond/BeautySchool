# Generated by Django 2.0 on 2020-03-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='account.png', upload_to='users/%Y/%m/%d'),
        ),
    ]

# Generated by Django 2.0 on 2020-03-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_review_studio_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='school_review',
            field=models.TextField(max_length=500),
        ),
    ]

# Generated by Django 2.0 on 2020-03-24 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='course.jpg', upload_to='courses/%Y/%m/%d'),
        ),
    ]

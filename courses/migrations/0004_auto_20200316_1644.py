# Generated by Django 2.0 on 2020-03-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_date_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]

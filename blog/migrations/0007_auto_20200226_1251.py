# Generated by Django 2.0 on 2020-02-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_files'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='post',
            name='photo_first',
            field=models.ImageField(blank=True, upload_to='blogs/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_second',
            field=models.ImageField(blank=True, upload_to='blogs/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_third',
            field=models.ImageField(blank=True, upload_to='blogs/%Y/%m/%d'),
        ),
    ]

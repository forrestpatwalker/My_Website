# Generated by Django 3.1.7 on 2021-03-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/my_website/img'),
        ),
    ]

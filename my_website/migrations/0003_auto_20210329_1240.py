# Generated by Django 3.1.7 on 2021-03-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0002_auto_20210329_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=150),
        ),
    ]
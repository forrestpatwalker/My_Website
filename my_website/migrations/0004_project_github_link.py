# Generated by Django 3.1.7 on 2021-03-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_website', '0003_auto_20210329_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(default='https://github.com/foorast'),
        ),
    ]
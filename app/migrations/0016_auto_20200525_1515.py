# Generated by Django 3.0.5 on 2020-05-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200525_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='files',
            field=models.ImageField(upload_to='media'),
        ),
    ]

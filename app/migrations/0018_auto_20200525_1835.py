# Generated by Django 3.0.5 on 2020-05-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200525_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='files',
            new_name='filess',
        ),
    ]
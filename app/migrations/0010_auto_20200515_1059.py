# Generated by Django 3.0.5 on 2020-05-15 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200515_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emaill',
            new_name='email',
        ),
    ]
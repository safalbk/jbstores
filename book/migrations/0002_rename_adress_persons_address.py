# Generated by Django 4.2.4 on 2023-08-17 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persons',
            old_name='adress',
            new_name='address',
        ),
    ]

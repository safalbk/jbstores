# Generated by Django 4.2.4 on 2023-08-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_adress_persons_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='account_balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='persons',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='persons',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

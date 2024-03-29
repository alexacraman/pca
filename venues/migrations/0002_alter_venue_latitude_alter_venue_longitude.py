# Generated by Django 4.2.6 on 2023-10-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=25, null=True),
        ),
    ]

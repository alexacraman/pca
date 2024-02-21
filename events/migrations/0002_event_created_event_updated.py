# Generated by Django 4.2.7 on 2024-01-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_committeemembers_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-21 20:28

from django.db import migrations, models
import django.db.models.deletion
import membership.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=120, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('county', models.CharField(blank=True, max_length=120, null=True)),
                ('post_code', models.CharField(max_length=9, validators=[membership.models.validate_postcode])),
            ],
        ),
        migrations.CreateModel(
            name='MembershipInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Mx', 'Mx'), ('Dr', 'Dr'), ('Prof', 'Prof')], max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('place_of_work_study', models.CharField(max_length=255)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('work_address', models.TextField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('qualification_status', models.CharField(choices=[('Student', 'Student'), ('Qualified', 'Qualified')], max_length=255)),
                ('qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('qualification_location', models.CharField(max_length=255)),
                ('year_of_qualification', models.DateField(blank=True, null=True)),
                ('other_qualifications', models.CharField(blank=True, max_length=255, null=True)),
                ('data_use_permission', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Expired', 'Expired'), ('Canceled', 'Canceled')], max_length=255)),
                ('paid', models.BooleanField(default=False)),
                ('stripe_id', models.CharField(blank=True, max_length=255)),
                ('subscription_id', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_id', models.URLField(blank=True, max_length=255, null=True)),
                ('customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('joined', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.membershipinterest')),
            ],
        ),
    ]
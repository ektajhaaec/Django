# Generated by Django 5.0.6 on 2024-05-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_city_profile_address_profile_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_number',
            field=models.CharField(default='Unknown', max_length=15),
        ),
    ]
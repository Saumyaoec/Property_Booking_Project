# Generated by Django 4.0.4 on 2022-05-03 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate_App', '0003_rename_bed_property_beds_alter_address_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_name',
            new_name='room_type_name',
        ),
    ]

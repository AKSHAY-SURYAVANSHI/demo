# Generated by Django 4.0.3 on 2022-07-06 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup_organization',
            old_name='Contact_Number_Organiztion',
            new_name='Contact_Number_Organization',
        ),
    ]

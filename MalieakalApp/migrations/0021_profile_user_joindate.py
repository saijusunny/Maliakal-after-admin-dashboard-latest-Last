# Generated by Django 4.0.2 on 2023-08-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0020_user_registration_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_user',
            name='joindate',
            field=models.DateField(null=True),
        ),
    ]

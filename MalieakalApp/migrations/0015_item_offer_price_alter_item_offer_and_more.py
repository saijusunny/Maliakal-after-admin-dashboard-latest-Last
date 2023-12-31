# Generated by Django 4.0.2 on 2023-08-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0014_offer_zone_offer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='offer_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='offer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='offer_zone',
            name='offer',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.2 on 2023-08-08 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0017_remove_checkout_item_remove_checkout_qty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout_item',
            name='item_total',
        ),
    ]
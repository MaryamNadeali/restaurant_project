# Generated by Django 3.2.9 on 2022-04-15 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_order_foods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='order_foods',
        ),
    ]

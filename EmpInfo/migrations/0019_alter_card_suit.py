# Generated by Django 3.2.1 on 2021-10-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpInfo', '0018_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.IntegerField(choices=[(1, 'Diamond'), (2, 'Spade'), (3, 'Heart'), (4, 'Club')], verbose_name='Suit'),
        ),
    ]

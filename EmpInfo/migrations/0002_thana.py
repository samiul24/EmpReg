# Generated by Django 3.2.1 on 2021-05-06 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('thana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmpInfo.district')),
            ],
        ),
    ]

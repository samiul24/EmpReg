# Generated by Django 3.2.1 on 2021-05-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpInfo', '0013_alter_empbasicinfo_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empbasicinfo',
            name='first_name',
            field=models.CharField(help_text='<b>Employee First Name</b>', max_length=50),
        ),
    ]

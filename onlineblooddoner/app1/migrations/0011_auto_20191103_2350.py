# Generated by Django 2.2.4 on 2019-11-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20191103_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='last_donate_date',
            field=models.TextField(default=False),
        ),
    ]

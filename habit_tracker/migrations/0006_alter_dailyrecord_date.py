# Generated by Django 4.0.3 on 2022-03-26 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0005_rename_record_dailyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='date',
            field=models.DateField(),
        ),
    ]

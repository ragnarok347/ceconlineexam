# Generated by Django 3.0.3 on 2020-03-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0021_auto_20200312_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='time',
        ),
        migrations.AddField(
            model_name='store',
            name='student',
            field=models.CharField(default='null', max_length=100),
        ),
    ]

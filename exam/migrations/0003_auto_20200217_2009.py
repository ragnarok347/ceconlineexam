# Generated by Django 3.0.3 on 2020-02-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20200217_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='types',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.0.3 on 2020-10-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newadmin', '0009_centre_head'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='publish_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='reg_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='exam',
            name='reg_start',
            field=models.DateField(null=True),
        ),
    ]
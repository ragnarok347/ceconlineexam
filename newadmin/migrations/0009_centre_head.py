# Generated by Django 3.0.3 on 2020-06-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newadmin', '0008_auto_20200530_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='centre',
            name='head',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

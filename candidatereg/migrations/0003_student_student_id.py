# Generated by Django 3.0.3 on 2020-04-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatereg', '0002_auto_20200430_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatereg', '0004_remove_student_sig'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registration_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

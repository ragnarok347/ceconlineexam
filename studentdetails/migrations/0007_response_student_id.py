# Generated by Django 3.0.3 on 2020-03-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdetails', '0006_response_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='student_id',
            field=models.CharField(default='null', max_length=20),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_question_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0027_delete_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='img',
            field=models.ImageField(upload_to='media\\pics'),
        ),
    ]
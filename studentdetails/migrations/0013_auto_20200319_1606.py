# Generated by Django 3.0.3 on 2020-03-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdetails', '0012_auto_20200319_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question1',
            name='img',
            field=models.ImageField(upload_to='esoft/media/'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-05-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0009_auto_20200526_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='cquestion',
            name='img',
            field=models.ImageField(default=0, upload_to='pics/'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0025_auto_20200312_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]

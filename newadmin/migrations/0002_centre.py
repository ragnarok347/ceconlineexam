# Generated by Django 3.0.3 on 2020-05-28 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=25, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('capacity', models.IntegerField(null=True)),
            ],
        ),
    ]

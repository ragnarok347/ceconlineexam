# Generated by Django 3.0.3 on 2020-05-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0004_auto_20200419_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verifier_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdetails', '0016_timer_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='null', max_length=50)),
                ('name', models.CharField(default='null', max_length=50)),
                ('dob', models.DateField(default='null')),
                ('exam_name', models.CharField(default='null', max_length=50)),
                ('mark', models.IntegerField(default='null')),
                ('total', models.IntegerField(default='null')),
                ('criteria', models.IntegerField(default='null')),
                ('qualify', models.BooleanField(default=False)),
            ],
        ),
    ]

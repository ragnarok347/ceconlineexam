# Generated by Django 3.0.3 on 2020-02-21 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0006_myuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]

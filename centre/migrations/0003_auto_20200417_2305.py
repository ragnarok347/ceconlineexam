# Generated by Django 3.0.3 on 2020-04-17 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0002_candidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='accepted_ans',
            new_name='answer',
        ),
    ]

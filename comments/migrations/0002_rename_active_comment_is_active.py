# Generated by Django 3.2.5 on 2021-07-22 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='is_active',
        ),
    ]

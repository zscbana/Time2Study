# Generated by Django 5.1.2 on 2024-10-14 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authors',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='data_posted',
            new_name='date_posted',
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-14 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_rfid_spaces_rename_rfid_spaces_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Spaces',
            new_name='Space',
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_rename_spaces_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='Username',
            field=models.CharField(max_length=20),
        ),
    ]

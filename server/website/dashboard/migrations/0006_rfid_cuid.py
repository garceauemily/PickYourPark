# Generated by Django 4.1.7 on 2023-04-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rfid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfid',
            name='CUID',
            field=models.CharField(default=11, max_length=9),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.4 on 2022-12-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_sensor_id_measurement_sensor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo_url',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
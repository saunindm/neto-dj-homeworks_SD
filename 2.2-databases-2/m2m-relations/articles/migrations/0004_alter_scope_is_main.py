# Generated by Django 4.1.3 on 2022-12-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
    ]

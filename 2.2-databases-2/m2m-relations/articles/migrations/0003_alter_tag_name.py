# Generated by Django 4.1.3 on 2022-12-01 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_alter_article_options_tag_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название'),
        ),
    ]
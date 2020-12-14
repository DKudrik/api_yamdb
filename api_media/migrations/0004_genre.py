# Generated by Django 3.0.5 on 2020-12-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_media', '0003_auto_20201213_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название жанра')),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2024-06-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_additional_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='banner_image',
            field=models.URLField(default='paste banner link here'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_link',
            field=models.URLField(default='paste banner link here '),
        ),
    ]

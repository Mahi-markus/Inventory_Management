# Generated by Django 5.1.3 on 2024-12-04 03:46

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invent_app', '0004_alter_location_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='center',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]

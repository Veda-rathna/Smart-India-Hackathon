# Generated by Django 5.1 on 2024-09-09 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue_app', '0003_queue_arrival_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queue_app.patient')),
            ],
        ),
    ]

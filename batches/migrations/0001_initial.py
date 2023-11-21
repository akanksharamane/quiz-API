# Generated by Django 3.2.19 on 2023-11-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.IntegerField()),
                ('batchType', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('batchTime', models.CharField(max_length=50)),
                ('seatAvailable', models.BooleanField()),
                ('duration', models.CharField(max_length=50)),
                ('batchStatus', models.CharField(max_length=50)),
            ],
        ),
    ]

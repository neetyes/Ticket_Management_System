# Generated by Django 2.0.7 on 2018-07-30 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20180730_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSE', 'Close'), ('PENDING', 'Pending')], max_length=10),
        ),
    ]

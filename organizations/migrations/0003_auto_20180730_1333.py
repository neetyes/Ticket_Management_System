# Generated by Django 2.0.7 on 2018-07-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20180727_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
    ]

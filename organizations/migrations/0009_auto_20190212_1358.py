# Generated by Django 2.0.7 on 2019-02-12 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0008_auto_20180819_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['name']},
        ),
    ]

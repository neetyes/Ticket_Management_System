# Generated by Django 2.0.7 on 2018-08-06 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_auto_20180806_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='contact',
            new_name='phone',
        ),
    ]

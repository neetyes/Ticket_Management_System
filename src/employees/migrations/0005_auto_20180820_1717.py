# Generated by Django 2.0.7 on 2018-08-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20180813_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
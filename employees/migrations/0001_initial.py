# Generated by Django 2.0.7 on 2018-08-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('contact_no', models.TextField(blank=True, max_length=254, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('position', models.CharField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-05 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='name',
        ),
    ]

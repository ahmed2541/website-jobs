# Generated by Django 4.1.1 on 2022-10-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]

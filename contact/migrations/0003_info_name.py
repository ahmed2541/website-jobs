# Generated by Django 4.1.1 on 2022-10-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_info_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

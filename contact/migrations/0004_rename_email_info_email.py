# Generated by Django 4.1.1 on 2022-10-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_info_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='email',
            new_name='Email',
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutadmin',
            name='image',
            field=models.ImageField(default='admin_photos/22/10/05/IMG_20220227_200036_660.jpg', upload_to='admin_photos/%y/%m/%d'),
        ),
    ]

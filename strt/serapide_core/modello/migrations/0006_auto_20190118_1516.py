# Generated by Django 2.0.8 on 2019-01-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modello', '0005_auto_20190118_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risorsa',
            name='file',
            field=models.FileField(max_length=500, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]

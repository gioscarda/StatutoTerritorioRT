# Generated by Django 2.0.8 on 2019-03-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modello', '0030_auto_20190308_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceduravas',
            name='pubblicazione_provvedimento_verifica_ac',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proceduravas',
            name='pubblicazione_provvedimento_verifica_ap',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.0.8 on 2019-02-15 14:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('modello', '0014_auto_20190213_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Azione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, null=True)),
                ('tipologia', models.CharField(choices=[('unknown', 'UNKNOWN'), ('creato_piano', 'Creato Piano'), ('parere_verifica_vas', 'Parere Verifica VAS'), ('richiesta_verifica_vas', 'Richiesta Verifica VAS'), ('avvio_procedimento', 'Avvio Procedimento'), ('formazione_del_piano', 'Formazione del Piano'), ('protocollo_genio_civile', 'Protocollo Genio Civile')], default='unknown', max_length=80)),
                ('attore', models.CharField(choices=[('unknown', 'UNKNOWN'), ('comune', 'Comune'), ('ac', 'AC'), ('sca', 'SCA'), ('genio_civile', 'Genio Civile')], default='unknown', max_length=80)),
                ('stato', models.CharField(choices=[('unknown', 'UNKNOWN'), ('nessuna', 'NESSUNA'), ('attesa', 'ATTESA'), ('necessaria', 'NECESSARIA')], default='unknown', max_length=20)),
                ('data', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='piano',
            name='tipologia',
            field=models.CharField(choices=[('unknown', 'UNKNOWN'), ('operativo', 'OPERATIVO'), ('strutturale', 'STRUTTURALE'), ('variante', 'VARIANTE')], default='unknown', max_length=80),
        ),
    ]

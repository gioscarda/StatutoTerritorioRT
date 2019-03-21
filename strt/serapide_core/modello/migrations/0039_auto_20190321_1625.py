# Generated by Django 2.0.8 on 2019-03-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modello', '0038_auto_20190321_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='azione',
            name='tipologia',
            field=models.CharField(choices=[('unknown', 'UNKNOWN'), ('creato_piano', 'Creato Piano'), ('richiesta_verifica_vas', 'Richiesta Verifica VAS'), ('pareri_verifica_sca', 'Pareri Verifica VAS'), ('emissione_provvedimento_verifica', 'Emissione Provvedimento di Verifica'), ('pubblicazione_provvedimento_verifica', 'Pubblicazione Provvedimento di Verifica'), ('avvio_consultazioni_sca', 'Avvio Consultazioni SCA'), ('pareri_sca', 'Pareri SCA'), ('avvio_esame_pareri_sca', 'Avvio Esame Pareri SCA'), ('upload_elaborati_vas', 'Upload Elaborati VAS'), ('avvio_procedimento', 'Avvio Procedimento'), ('formazione_del_piano', 'Formazione del Piano'), ('protocollo_genio_civile', 'Protocollo Genio Civile'), ('richiesta_conferenza_copianificazione', 'Convocazione Conferenza di Copianificazione'), ('convocazione_conferenza_copianificazione', 'Convocazione Conferenza di Copianificazione'), ('osservazioni_enti', 'Osservazioni Enti'), ('osservazioni_regione', 'Osservazioni Regione'), ('upload_osservazioni_privati', 'Upload Osservazioni Privati')], default='unknown', max_length=80),
        ),
    ]

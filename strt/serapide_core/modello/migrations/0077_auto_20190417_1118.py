# Generated by Django 2.0.8 on 2019-04-17 11:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('strt_users', '0006_auto_20190215_1022'),
        ('modello', '0076_auto_20190417_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProceduraAdozioneVAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, null=True)),
                ('tipologia', models.CharField(choices=[('unknown', 'UNKNOWN'), ('semplificata', 'SEMPLIFICATA'), ('verifica', 'VERIFICA'), ('procedimento', 'PROCEDIMENTO'), ('procedimento_semplificato', 'PROCEDIMENTO_SEMPLIFICATO'), ('non_necessaria', 'NON_NECESSARIA')], default='unknown', max_length=50)),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('conclusa', models.BooleanField(default=False)),
                ('ente', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='strt_users.Organization', verbose_name='ente')),
                ('piano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modello.Piano')),
            ],
            options={
                'db_table': 'strt_core_adozione_vas',
                'verbose_name_plural': 'Procedure Adozione VAS',
            },
        ),
        migrations.CreateModel(
            name='RisorseAdozioneVas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedura_adozione_vas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modello.ProceduraAdozioneVAS')),
                ('risorsa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modello.Risorsa')),
            ],
            options={
                'db_table': 'strt_core_adozione_vas_risorse',
            },
        ),
        migrations.AlterField(
            model_name='azione',
            name='tipologia',
            field=models.CharField(choices=[('unknown', 'UNKNOWN'), ('creato_piano', 'Creato Piano/Variante'), ('richiesta_verifica_vas', 'Documento Preliminare VAS'), ('pareri_verifica_sca', 'Pareri verifica VAS'), ('emissione_provvedimento_verifica', 'Emissione Provvedimento di verifica'), ('pubblicazione_provvedimento_verifica', 'Pubblicazione provvedimento di verifica'), ('avvio_consultazioni_sca', 'Avvio consultazioni SCA'), ('pareri_sca', 'Pareri SCA'), ('avvio_esame_pareri_sca', 'Avvio esame pareri SCA'), ('upload_elaborati_vas', 'Upload elaborati VAS'), ('avvio_procedimento', 'Avvio del Procedimento'), ('richiesta_integrazioni', 'Richiesta Integrazioni'), ('integrazioni_richieste', 'Integrazioni Richieste'), ('formazione_del_piano', 'Formazione del Piano'), ('protocollo_genio_civile', 'Protocollo Genio Civile'), ('protocollo_genio_civile_id', 'Protocollo N.'), ('richiesta_conferenza_copianificazione', 'Richiesta Conferenza di copianificazione'), ('esito_conferenza_copianificazione', 'Esito conferenza di copianificazione'), ('trasmissione_adozione', 'Trasmissione Adozione'), ('osservazioni_enti', 'Osservazioni Enti'), ('osservazioni_regione', 'Osservazioni Regione'), ('upload_osservazioni_privati', 'Upload Osservazioni Privati'), ('controdeduzioni', 'Controdeduzioni'), ('piano_controdedotto', 'Piano Controdedotto'), ('esito_conferenza_paesaggistica', 'Esiti conferenza paesaggistica'), ('rev_piano_post_cp', 'Revisione Piano post Conf. Paesaggistica'), ('pareri_adozione_sca', 'Pareri SCA'), ('parere_motivato_ac', 'Parere Motivato'), ('trasmissione_approvazione', 'Invio documentazione per Approvazione')], default='unknown', max_length=80),
        ),
        migrations.AddField(
            model_name='proceduraadozionevas',
            name='risorse',
            field=models.ManyToManyField(through='modello.RisorseAdozioneVas', to='modello.Risorsa'),
        ),
    ]

# Generated by Django 2.0.8 on 2019-02-13 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strt_users', '0004_token_expires'),
        ('modello', '0013_contatto_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PianoAuthTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modello.Piano')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strt_users.Token')),
            ],
            options={
                'db_table': 'strt_core_piano_auth_tokens',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pianoauthtokens',
            unique_together={('piano', 'token')},
        ),
    ]
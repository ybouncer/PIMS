# Generated by Django 5.0.3 on 2024-04-03 18:08

import django.db.models.deletion
import polls.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('idpersonne', models.AutoField(db_column='idpersonne', primary_key=True, serialize=False)),
                ('nom', models.TextField(db_column='nom')),
                ('prenom', models.TextField(db_column='prenom')),
                ('mail', models.TextField(db_column='mail', unique=True, validators=[polls.models.validate_email])),
                ('password', models.TextField(db_column='password')),
                ('role', models.JSONField(blank=True, db_column='role', default=list, null=True)),
                ('last_login', models.DateTimeField(blank=True, db_column='last_login', null=True)),
                ('is_superuser', models.BooleanField(db_column='is_superuser', default=False)),
            ],
            options={
                'db_table': 'personne',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idcours', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.TextField(db_column='nom')),
            ],
            options={
                'db_table': 'cours',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('idetudiant', models.AutoField(db_column='idetudiant', primary_key=True, serialize=False)),
                ('bloc', models.IntegerField(db_column='bloc', validators=[polls.models.validate_block])),
            ],
            options={
                'db_table': 'etudiant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('idinscription', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'inscription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('idperiode', models.AutoField(db_column='idperiode', primary_key=True, serialize=False)),
                ('annee', models.IntegerField(db_column='annee')),
            ],
            options={
                'db_table': 'periode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('idprof', models.AutoField(db_column='idprof', primary_key=True, serialize=False)),
                ('specialite', models.TextField(db_column='specialite')),
            ],
            options={
                'db_table': 'professeur',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sujet',
            fields=[
                ('idsujet', models.AutoField(db_column='idsujet', primary_key=True, serialize=False)),
                ('titre', models.TextField(db_column='titre')),
                ('descriptif', models.TextField(db_column='descriptif')),
                ('destination', models.TextField(db_column='destination')),
                ('estPris', models.BooleanField(db_column='estPris', default=False)),
                ('fichier', models.FileField(blank=True, db_column='fichier', null=True, upload_to='sujets/', validators=[polls.models.validate_file_extension])),
            ],
            options={
                'db_table': 'sujet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ue',
            fields=[
                ('idue', models.TextField(db_column='idue', primary_key=True, serialize=False)),
                ('nom', models.TextField(db_column='nom')),
            ],
            options={
                'db_table': 'ue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivrable',
            fields=[
                ('idDelivrable', models.AutoField(db_column='iddelivrable', primary_key=True, serialize=False)),
                ('fichier', models.FileField(blank=True, db_column='fichier', null=True, upload_to=polls.models.get_upload_path)),
                ('typeFichier', models.TextField(db_column='typefichier', validators=[polls.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('idEtape', models.AutoField(db_column='idetape', primary_key=True, serialize=False)),
                ('delai', models.DateTimeField(db_column='delai')),
                ('description', models.TextField(db_column='description')),
                ('idDelivrable', models.ForeignKey(db_column='iddelivrable', on_delete=django.db.models.deletion.DO_NOTHING, to='polls.delivrable')),
                ('idPeriode', models.ForeignKey(db_column='idperiode', on_delete=django.db.models.deletion.DO_NOTHING, to='polls.periode')),
            ],
        ),
    ]

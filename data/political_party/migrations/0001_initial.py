# Generated by Django 3.0 on 2020-10-04 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0002_auto_20190520_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalParty',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('full_name', models.CharField(max_length=256, null=True)),
                ('environment', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='politicalparty_relation', to='environment.Environment')),
            ],
            options={
                'verbose_name': 'political party',
                'verbose_name_plural': 'political parties',
                'db_table': 'fec_political_party',
                'ordering': ['full_name'],
                'abstract': False,
                'unique_together': {('environment', 'name')},
            },
        ),
    ]

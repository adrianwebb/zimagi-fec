# Generated by Django 3.2.5 on 2021-07-13 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contributor', '0001_initial'),
        ('committee', '0001_initial'),
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(max_length=256, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('amount', models.FloatField(null=True)),
                ('committee', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_relation', to='committee.committee')),
                ('contributor', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_relation', to='contributor.contributor')),
                ('year', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_relation', to='year.year')),
            ],
            options={
                'verbose_name': 'receipt',
                'verbose_name_plural': 'receipts',
                'db_table': 'fec_receipt',
                'ordering': ['contributor_id', 'year__name', 'amount'],
                'abstract': False,
                'unique_together': {('committee', 'contributor', 'transaction_id')},
            },
        ),
    ]

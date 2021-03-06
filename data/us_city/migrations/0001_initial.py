# Generated by Django 3.2.5 on 2021-07-13 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us_state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USCity',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('state', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uscity_relation', to='us_state.usstate')),
            ],
            options={
                'verbose_name': 'us city',
                'verbose_name_plural': 'us cities',
                'db_table': 'fec_us_city',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('state', 'name')},
            },
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
            ],
            options={
                'verbose_name': 'employer',
                'verbose_name_plural': 'employers',
                'db_table': 'fec_employer',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]

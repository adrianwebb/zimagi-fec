# Generated by Django 3.0 on 2020-10-04 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0005_remove_receipt_candidate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receipt',
            options={'ordering': ['contributor_id', 'year__name', 'amount'], 'verbose_name': 'receipt', 'verbose_name_plural': 'receipts'},
        ),
    ]

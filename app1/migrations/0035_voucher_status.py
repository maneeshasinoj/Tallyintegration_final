# Generated by Django 4.0.4 on 2022-09-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_tally_ledger_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='status',
            field=models.CharField(default='null', max_length=255),
        ),
    ]

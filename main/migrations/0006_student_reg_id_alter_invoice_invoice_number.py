# Generated by Django 5.1 on 2024-12-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_invoice_invoice_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reg_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='F555233A', max_length=100, unique=True),
        ),
    ]

# Generated by Django 5.2 on 2025-05-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_service_record_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]

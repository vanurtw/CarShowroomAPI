# Generated by Django 5.2 on 2025-04-29 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

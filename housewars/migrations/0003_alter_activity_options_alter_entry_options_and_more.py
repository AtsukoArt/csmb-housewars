# Generated by Django 4.0.4 on 2022-05-16 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housewars', '0002_alter_activity_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterModelTable(
            name='activity',
            table=None,
        ),
    ]
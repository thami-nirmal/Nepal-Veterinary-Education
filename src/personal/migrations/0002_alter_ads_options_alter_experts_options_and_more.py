# Generated by Django 4.0 on 2023-05-18 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ads',
            options={'verbose_name_plural': 'Ads'},
        ),
        migrations.AlterModelOptions(
            name='experts',
            options={'verbose_name_plural': 'Expert'},
        ),
        migrations.AlterModelOptions(
            name='krishidiarys',
            options={'verbose_name_plural': 'Krishi Diary'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name_plural': 'Notice'},
        ),
    ]

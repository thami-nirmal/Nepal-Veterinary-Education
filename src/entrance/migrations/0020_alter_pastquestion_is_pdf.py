# Generated by Django 4.2.1 on 2023-05-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0019_remove_modelquestion_year_modelquestion_model_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastquestion',
            name='is_pdf',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-21 05:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_graduate', '0003_alter_loksewanotes_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='councilmodelquestion',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='councilpastquestion',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='loksewamodelquestion',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='loksewanotes',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='loksewapastquestion',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-22 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrance', '0010_gk_seo_description_gk_seo_image_gk_seo_keyword_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gk',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='gk',
            name='seo_image',
        ),
        migrations.RemoveField(
            model_name='gk',
            name='seo_keyword',
        ),
        migrations.RemoveField(
            model_name='gk',
            name='seo_title',
        ),
        migrations.RemoveField(
            model_name='modelquestion',
            name='seo_description',
        ),
        migrations.RemoveField(
            model_name='modelquestion',
            name='seo_image',
        ),
        migrations.RemoveField(
            model_name='modelquestion',
            name='seo_keyword',
        ),
        migrations.RemoveField(
            model_name='modelquestion',
            name='seo_title',
        ),
    ]

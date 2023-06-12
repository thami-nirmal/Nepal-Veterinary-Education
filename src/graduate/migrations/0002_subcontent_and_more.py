# Generated by Django 4.2.1 on 2023-06-11 09:39

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_content_name', models.CharField(blank=True, max_length=80)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('pdf_URL', models.URLField(default='', max_length=220)),
                ('is_pdf', models.BooleanField(default=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Chapter',
            },
        ),
        migrations.RenameField(
            model_name='materialcontent',
            old_name='sub_content',
            new_name='has_sub_content',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.AddField(
            model_name='subcontent',
            name='material_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_materialcontent', to='graduate.materialcontent'),
        ),
    ]

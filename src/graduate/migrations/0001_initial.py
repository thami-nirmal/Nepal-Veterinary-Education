# Generated by Django 4.2.1 on 2023-06-06 11:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Level',
            },
        ),
        migrations.CreateModel(
            name='SemYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem_year_num', models.PositiveSmallIntegerField(null=True)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('is_year', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SemYear_Level', to='graduate.level')),
            ],
            options={
                'verbose_name_plural': 'Semester Year',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_level', to='graduate.level')),
                ('sem_year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject_semyear', to='graduate.semyear')),
            ],
            options={
                'verbose_name_plural': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MaterialType_Level', to='graduate.level')),
            ],
            options={
                'verbose_name_plural': 'Material Type',
                'db_table': 'Material Type',
            },
        ),
        migrations.CreateModel(
            name='MaterialContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_chapter_content', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('pdf_URL', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
                ('material_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materialcontent_materialtype', to='graduate.materialtype')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materialcontent_subject', to='graduate.subject')),
            ],
            options={
                'verbose_name_plural': 'Material Content',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_no', models.PositiveSmallIntegerField(null=True)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('pdf_URL', models.URLField(default='', max_length=220)),
                ('is_pdf', models.BooleanField(default=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
                ('material_content', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapter_materialcontent', to='graduate.materialcontent')),
            ],
            options={
                'verbose_name_plural': 'Chapter',
            },
        ),
    ]

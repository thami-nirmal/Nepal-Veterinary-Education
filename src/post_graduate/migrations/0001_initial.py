# Generated by Django 4.2.1 on 2023-06-02 05:31

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_choices', models.CharField(choices=[('AFU', 'Agriculture and Forestry University'), ('TU', 'Tribhuvan University'), ('PU', 'Purwanchal University')], default='', max_length=100)),
                ('faculty_choices', models.CharField(choices=[('B.V.Sc and A.H', 'B.V.Sc and A.H / B.Sc Fisheries'), ('B.Sc Agriculture', 'B.Sc Agriculture'), ('B.Sc Forestry', 'B.Sc Forestry')], default='', max_length=100)),
                ('quota_name', models.CharField(blank=True, max_length=50)),
                ('no_of_student', models.PositiveSmallIntegerField(null=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'College Info',
            },
        ),
        migrations.CreateModel(
            name='CouncilAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('pdf_url', models.URLField()),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Council Act',
            },
        ),
        migrations.CreateModel(
            name='CouncilModelQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('is_shown', models.BooleanField(default=True)),
                ('pdf_url', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Council Model Question',
            },
        ),
        migrations.CreateModel(
            name='CouncilPastQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_shown', models.BooleanField(default=True)),
                ('year', models.PositiveIntegerField(null=True)),
                ('pdf_url', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('types', models.CharField(blank=True, max_length=60)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Council Past Question',
            },
        ),
        migrations.CreateModel(
            name='CouncilRegulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('pdf_url', models.URLField()),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Council Regulation',
            },
        ),
        migrations.CreateModel(
            name='LoksewaModelQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('is_shown', models.BooleanField(default=True)),
                ('pdf_url', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Loksewa Model Question',
            },
        ),
        migrations.CreateModel(
            name='LoksewaNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('is_shown', models.BooleanField(default=True)),
                ('pdf_url', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Loksewa Note',
            },
        ),
        migrations.CreateModel(
            name='LoksewaPastQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_shown', models.BooleanField(default=True)),
                ('year', models.PositiveIntegerField(null=True)),
                ('pdf_url', models.URLField()),
                ('is_pdf', models.BooleanField(default=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('types', models.CharField(blank=True, max_length=60)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Loksewa Past Question',
            },
        ),
        migrations.CreateModel(
            name='SyllabusInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_choices', models.CharField(blank=True, choices=[('AFU', 'Agriculture and Forestry University'), ('TU', 'Tribhuvan University'), ('PU', 'Purwanchal University')], max_length=100)),
                ('faculty_choices', models.CharField(blank=True, choices=[('B.V.Sc and A.H', 'B.V.Sc and A.H / B.Sc Fisheries'), ('B.Sc Agriculture', 'B.Sc Agriculture'), ('B.Sc Forestry', 'B.Sc Forestry')], max_length=100)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('no_of_question', models.PositiveIntegerField(null=True)),
                ('marks', models.PositiveSmallIntegerField(null=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keyword', models.CharField(blank=True, max_length=200)),
                ('seo_image', models.ImageField(blank=True, null=True, upload_to='seo_images/')),
                ('seo_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Syllabus Info',
            },
        ),
    ]

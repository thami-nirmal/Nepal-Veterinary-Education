# Generated by Django 4.2.1 on 2023-08-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='feature_images/'),
        ),
    ]

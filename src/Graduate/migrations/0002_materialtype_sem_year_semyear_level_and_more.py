# Generated by Django 4.2.1 on 2023-05-16 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Graduate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='sem_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MaterialType_SemYear', to='Graduate.semyear'),
        ),
        migrations.AddField(
            model_name='semyear',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SemYear_Level', to='Graduate.level'),
        ),
        migrations.AddField(
            model_name='subject',
            name='material_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Subject_MaterialType', to='Graduate.materialtype'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Chapter_Subject', to='Graduate.subject'),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_projectform_dev_fifth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectform',
            name='first_task_duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='first_task_ending',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='first_task_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='first_task_starting',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='second_task_duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='second_task_ending',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='second_task_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='second_task_starting',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='third_task_duration',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='third_task_ending',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='third_task_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='third_task_starting',
            field=models.DateField(blank=True, null=True),
        ),
    ]

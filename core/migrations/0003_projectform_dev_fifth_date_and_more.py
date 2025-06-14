# Generated by Django 5.1.7 on 2025-03-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_projectform_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectform',
            name='dev_fifth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_fifth_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_first_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_fourth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_fourth_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_second_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_second_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_sixth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_sixth_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_third_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectform',
            name='dev_third_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

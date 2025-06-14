# Generated by Django 5.1.7 on 2025-06-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_projectform_c_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectform',
            old_name='it_business_name',
            new_name='it_business_partener',
        ),
        migrations.RenameField(
            model_name='projectform',
            old_name='it_business_sig',
            new_name='it_pmo_manager',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_pmo_name',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_pmo_sig',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_project_name',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_project_sig',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_service_name',
        ),
        migrations.RemoveField(
            model_name='projectform',
            name='it_service_sig',
        ),
        migrations.AddField(
            model_name='projectform',
            name='it_business_partener_sig',
            field=models.FileField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AddField(
            model_name='projectform',
            name='it_pmo_manager_sig',
            field=models.FileField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AddField(
            model_name='projectform',
            name='it_project_manager_sig',
            field=models.FileField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AddField(
            model_name='projectform',
            name='it_service_owner_manager_sig',
            field=models.FileField(blank=True, null=True, upload_to='signatures/'),
        ),
        migrations.AlterField(
            model_name='projectform',
            name='business_sig',
            field=models.FileField(blank=True, null=True, upload_to='signatures/'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_components_name_remove_projects_components_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='components',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]

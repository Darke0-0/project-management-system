# Generated by Django 4.2.4 on 2023-08-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_components_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='components',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
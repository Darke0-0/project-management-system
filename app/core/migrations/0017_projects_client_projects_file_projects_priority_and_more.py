# Generated by Django 4.2.4 on 2023-08-20 13:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_components_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='client',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='projects',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='projects',
            name='priority',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='projects',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='user_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='costing',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.DeleteModel(
            name='Components',
        ),
    ]

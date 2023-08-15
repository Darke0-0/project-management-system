# Generated by Django 4.2.4 on 2023-08-13 05:37

import core.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_project_groupmessage_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='pair',
            new_name='room',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='sender',
        ),
        migrations.AddField(
            model_name='chat',
            name='room_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='messages',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.RemoveField(
            model_name='messages',
            name='reciever',
        ),
        migrations.AddField(
            model_name='messages',
            name='reciever',
            field=models.CharField(null=True, verbose_name=core.models.User),
        ),
    ]

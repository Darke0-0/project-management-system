# Generated by Django 4.2.4 on 2023-08-09 18:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_chat_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='users',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='sender',
        ),
        migrations.AddField(
            model_name='messages',
            name='reciever',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

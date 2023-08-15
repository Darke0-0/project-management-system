# Generated by Django 4.2.4 on 2023-08-13 08:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_chat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='reciever',
        ),
        migrations.AddField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

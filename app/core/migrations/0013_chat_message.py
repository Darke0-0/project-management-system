# Generated by Django 4.2.4 on 2023-08-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_chat_room_name_alter_messages_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='message',
            field=models.ManyToManyField(blank=True, to='core.messages'),
        ),
    ]

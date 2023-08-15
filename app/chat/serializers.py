"""
Serializers for project APIs
"""
from rest_framework import serializers

from core.models import (
    Chat,
    Messages,
)

class MsgSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Messages
        fields = ['id','sender' ,'content','timestamp']
        read_only_fields = ['id']

class ChatSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    msgs = MsgSerializer(many=True, required=True)

    class Meta:
        model = Chat
        fields = [
            'id', 'room_name','user', 'msgs'
        ]
        read_only_fields = ['id']

    def _get_or_create_msgs(self, msgs, project):
        """Handle getting or creating msgs as needed."""
        for msg in msgs:
            msg_obj, created = Messages.objects.get_or_create(
                **msg,
            )
            project.msgs.add(msg_obj)

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        chat = Chat.objects.create(**validated_data)
        msgs = validated_data.pop('msgs', [])
        self._get_or_create_msgs(msgs, chat)
        return chat

class GroupMsgSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Messages
        fields = ['id', 'room','content','timestamp']
        read_only_fields = ['id']

class GroupChatSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""
    grpmsgs = GroupMsgSerializer(many=True, required=True)

    class Meta:
        model = Chat
        fields = [
            'id', 'project','users','grpmsgs'
        ]
        read_only_fields = ['id']

    def _get_or_create_msgs(self, msgs, project):
        """Handle getting or creating msgs as needed."""
        for msg in msgs:
            msg_obj, created = Messages.objects.get_or_create(
                **msg,
            )
            project.msgs.add(msg_obj)

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        chat = Chat.objects.create(**validated_data)
        msgs = validated_data.pop('msgs', [])
        self._get_or_create_msgs(msgs, chat)
        return chat

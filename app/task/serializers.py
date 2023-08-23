from rest_framework import serializers

from core.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id', 'project', 'start_date', 'users', 'heading',
            'end_date', 'description', 'priority', 'file'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a project."""
        project = Task.objects.create(**validated_data)

        return project

    def update(self, instance, validated_data):
        """Update project."""

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
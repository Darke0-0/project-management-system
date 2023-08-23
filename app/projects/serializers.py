"""
Serializers for project APIs
"""
from rest_framework import serializers

from core.models import Projects

class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = [
            'id', 'title', 'start_date', 'users',
            'end_date', 'team_lead', 'costing',
            'description', 'client', 'priority', 'file'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a project."""
        project = Projects.objects.create(**validated_data)

        return project

    def update(self, instance, validated_data):
        """Update project."""

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class ProjectsDetailSerializer(ProjectsSerializer):
    """Serializer for project detail view."""

    class Meta(ProjectsSerializer.Meta):
        fields = ProjectsSerializer.Meta.fields + ['description']
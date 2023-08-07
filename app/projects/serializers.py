"""
Serializers for project APIs
"""
from rest_framework import serializers

from core.models import (
    Projects,
    Tag,
    Components,
)

class ComponentsSerializer(serializers.ModelSerializer):
    """Serializer for components."""

    class Meta:
        model = Components
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

# Create your tests here.
class ProjectsSerializer(serializers.ModelSerializer):
    """Serializer for projects."""
    tags = TagSerializer(many=True, required=False)
    components = ComponentsSerializer(many=True, required=False)

    class Meta:
        model = Projects
        fields = [
            'id', 'title', 'start_date', 'end_date',
            'tags','components',
        ]
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, project):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            project.tags.add(tag_obj)

    def _get_or_create_components(self, components, project):
        """Handle getting or creating components as needed."""
        auth_user = self.context['request'].user
        for component in components:
            component_obj, created = Components.objects.get_or_create(
                user=auth_user,
                **component,
            )
            project.components.add(component_obj)

    def create(self, validated_data):
        """Create a project."""
        tags = validated_data.pop('tags', [])
        components = validated_data.pop('components', [])
        project = Projects.objects.create(**validated_data)
        self._get_or_create_tags(tags, project)
        self._get_or_create_components(components, project)

        return project

    def update(self, instance, validated_data):
        """Update project."""
        tags = validated_data.pop('tags', None)
        components = validated_data.pop('components', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
        if components is not None:
            instance.components.clear()
            self._get_or_create_components(components, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class ProjectsDetailSerializer(ProjectsSerializer):
    """Serializer for project detail view."""

    class Meta(ProjectsSerializer.Meta):
        fields = ProjectsSerializer.Meta.fields + ['description']
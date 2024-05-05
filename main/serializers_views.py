from rest_framework import serializers as drf_serializers
from main.models import Themes, Subtopics


class ThemesSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = ['name']


class SubtopicsSerializer(drf_serializers.ModelSerializer):
    name_themes = ThemesSerializer()

    class Meta:
        model = Subtopics
        fields = ['name_themes', 'name']

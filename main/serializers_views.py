from rest_framework import serializers as drf_serializers
from main.models import Themes, Subtopics, Items


class ItemsSerializer(drf_serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['name']


class ThemesSerializer(drf_serializers.ModelSerializer):
    name_items = ItemsSerializer()

    class Meta:
        model = Themes
        fields = ['name', 'name_items']


class SubtopicsSerializer(drf_serializers.ModelSerializer):
    name_themes = ThemesSerializer()

    class Meta:
        model = Subtopics
        fields = ['name_themes', 'name']

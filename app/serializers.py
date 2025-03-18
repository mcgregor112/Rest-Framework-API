from rest_framework import serializers
from app.models import *

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = snipated
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
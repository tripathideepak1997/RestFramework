from rest_framework import serializers
from .models import Questions, Choices


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('text', 'owner')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ('question', 'text')
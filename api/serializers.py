from rest_framework import serializers
from .models import Answers

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers 
        fields = ('id', 'host', 'mainGenre', 'secGenre', 'yearOfRelease', 'checkedAt')

class ChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ('mainGenre', 'secGenre', 'yearOfRelease')
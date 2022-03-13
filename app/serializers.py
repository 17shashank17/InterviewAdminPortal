from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class InterviewerSerializer(serializers.ModelSerializer):
    examiner = UserSerializer(read_only=True)
    class Meta:
        model = models.Interviewer
        fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    class Meta:
        model = models.Participants
        fields = "__all__"

class InterviewSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    interviewer = InterviewerSerializer(many=True)
    participants = ParticipantSerializer(many=True)
    class Meta:
        model = models.Interview
        fields = "__all__"



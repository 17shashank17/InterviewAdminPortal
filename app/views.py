from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from . import serializers
from rest_framework.response import Response
from . models import *
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    parser_classes
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class InterviewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = serializers.InterviewSerializer

class InterviewerListViewSet(viewsets.ModelViewSet):
    queryset = Interviewer.objects.all()
    serializer_class = serializers.InterviewerSerializer


@api_view(["POST"])
def addParticipants(request):
    data = request.data
    print(data)
    participants = data["participants"]
    compId = data["competitionId"]
    interview = Interview.objects.get(competitionId=compId)
    for participant in participants:
        user = User.objects.get(username=participant)
        try:
            part = Participants.objects.get(student=user)
        except:
            part = Participants(student=user)
        part.save()
        interview.participants.add(part)
    interview.save()
    
    return Response(data=serializers.InterviewSerializer(interview).data, status=status.HTTP_200_OK)
    
@api_view(["POST"])
def addInterviewer(request):
    data = request.data
    print(data)
    interviewers = data["interviewers"]
    compId = data["competitionId"]
    interview = Interview.objects.get(competitionId=compId)
    for interviewer in interviewers:
        user = User.objects.get(username=interviewer)
        try:
            intview = Interviewer.objects.get(examiner=user)
        except:
            intview = Interviewer(examiner=user)

        intview.save()
        interview.interviewer.add(intview)
    interview.save()
    
    return Response(data=serializers.InterviewSerializer(interview).data, status=status.HTTP_200_OK)

@api_view(["POST"])
def checkIfSlotAvailableForParticipant(request):
    data = request.data
    userId = data["username"]
    user = User.objects.get(username=userId)
    participant = Participants.objects.get(student=user)
    interviewListOfUser = Interview.objects.filter(participants=participant)

    slot_start_ts = data["slot_start_ts"]
    slot_end_ts = data["slot_end_ts"]

    for interview in interviewListOfUser:
        if slot_start_ts < interview.startTime and slot_end_ts < interview.startTime:
            return Response(data={"status": True}, status=status.HTTP_200_OK)
        elif slot_start_ts > interview.endTime:
            return Response(data={"status": True}, status=status.HTTP_200_OK)
    
    return Response(data={"status": False}, status=status.HTTP_200_OK)
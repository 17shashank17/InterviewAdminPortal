from django.db import models
from django.contrib.auth.models import User
import time, uuid

# Create your models here.


class Interviewer(models.Model):
    examiner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, default="+91 xxxxxxxxxx", blank=False)
    experience = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.examiner.username

class Participants(models.Model):
    student = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20, default="+91 xxxxxxxxxx", blank=False)
    badge = models.PositiveIntegerField(default=1, blank=False)

    def __str__(self):
        return self.student.username

class Interview(models.Model):
    organization = models.CharField(max_length=20, blank=False)
    orgId = models.UUIDField(default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=20, blank=False, default="Default Competetion")
    competitionId = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    difficulty = models.CharField(default="Easy", blank=True, max_length=20)
    isPublic = models.BooleanField(max_length=20, default=True, blank=False)
    startTime = models.CharField(max_length=20, blank=False, default=str(int(time.time())*1000))
    endTime = models.CharField(max_length=20, blank=False, default=str(int(time.time())*1000))
    update_at = models.CharField(max_length=20, blank=False, default=str(int(time.time())*1000) , editable=False)
    description = models.CharField(max_length=1000, blank=False, default="")
    interviewer = models.ManyToManyField(Interviewer, related_name="interviewer", blank=False)
    participants = models.ManyToManyField(Participants, blank=False)

    def __str__(self):
        return f'Competetion Name = {self.name}, Organization = {self.organization}'


class Question(models.Model):
    interview = models.ForeignKey(Interview, blank=False, on_delete=models.CASCADE)
    question = models.CharField(max_length=50, blank=False)
    questionType = models.CharField(blank=False, max_length=50)
    options = models.CharField(blank=False, max_length=50)
    options = models.CharField(blank=False, max_length=50)



from django.db import models
from exams.models import Exams
#from sounds.models import Sounds
from partofspeech.models import PartOfSpeechs
from user.models import CustomerUser
# Create your models here.


class Topic(models.Model):
    Chude= models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        #return self.Chude
        return f"{self.id}, {self.Chude}"


class Reading(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    NoiDungTA = models.CharField(max_length=9999, blank=True, null=True)
    NoiDungTV = models.CharField(max_length=9999, blank=True, null=True)
    Exams = models.ForeignKey(Exams, on_delete=models.CASCADE)


class Speaking(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    CachDoc = models.CharField(max_length=255, blank=True, null=True)
    DapAn = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.DapAn


class Listening(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Sound = models.CharField(max_length=255, blank=True, null=True)
    CauHoi = models.CharField(max_length=255, blank=True, null=True)
    DapAn = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        #return self.Chude
        return f"{self.id}"



class NewWords(models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Sound = models.CharField(max_length=255, blank=True, null=True)
    TenTA = models.CharField(max_length=255, blank=True, null=True)
    NghiaTV = models.CharField(max_length=255, blank=True, null=True)
    PoS = models.ForeignKey(PartOfSpeechs, on_delete=models.CASCADE)
    VdTA = models.CharField(max_length=255, blank=True, null=True)
    VdTV = models.CharField(max_length=255, default=0)
    PhatAm = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.TenTA


class OldWords(models.Model):
    NewWords = models.ForeignKey(NewWords, on_delete=models.CASCADE)
    User = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)


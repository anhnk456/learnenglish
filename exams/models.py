from django.db import models

# Create your models here.


class Exams(models.Model):
    TenExam = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.TenExam


class examsktra(models.Model):
    TenExam = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.TenExam


class questionktra(models.Model):
    Exams = models.ForeignKey(Exams, on_delete=models.CASCADE)
    CauHoi = models.CharField(max_length=9999, null=False, blank=False)
    Diem = models.IntegerField(default=0)
    DapAnDung = models.CharField(max_length=255, null=True, blank=True)
    DapAnA = models.CharField(max_length=255, null=True, blank=True)
    DapAnB = models.CharField(max_length=255, null=True, blank=True)
    DapAnC = models.CharField(max_length=255, null=True, blank=True)
    DapAnD = models.CharField(max_length=255, null=True, blank=True)


class Questions(models.Model):
    Exams = models.ForeignKey(Exams, on_delete=models.CASCADE)
    CauHoi = models.CharField(max_length=9999, null=False, blank=False)
    Diem = models.IntegerField(default=0)
    DapAnDung = models.CharField(max_length=255, null=True, blank=True)
    DapAnA = models.CharField(max_length=255, null=True, blank=True)
    DapAnB = models.CharField(max_length=255, null=True, blank=True)
    DapAnC = models.CharField(max_length=255, null=True, blank=True)
    DapAnD = models.CharField(max_length=255, null=True, blank=True)


class Choices(models.Model):
    Question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    DapAn = models.CharField(max_length=255, blank=False, null=False)
    DapAnDung = models.CharField(max_length=255, blank=False, null=False)


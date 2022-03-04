from django.db import models
from exams.models import Exams
# Create your models here.


class Grammars(models.Model):
    TenNguPhap = models.CharField(max_length=255, blank=False, null=False)
    NoiDung = models.CharField(max_length=99999, blank=True, null=True)
    Exams = models.ForeignKey(Exams, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenNguPhap



# class NguPhap(models.Model):
#     TenNguPhap = models.CharField(Grammars, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.TenNguPhap
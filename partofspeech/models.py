from django.db import models

# Create your models here.


class PartOfSpeechs(models.Model):
    Tuloai = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        # return self.Chude
        return f"{self.id}, {self.Tuloai}"
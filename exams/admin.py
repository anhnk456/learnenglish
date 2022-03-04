from django.contrib import admin
from .models import Exams, Questions, Choices
# Register your models here.

admin.site.register(Exams)
admin.site.register(Questions)
admin.site.register(Choices)
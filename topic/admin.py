from django.contrib import admin
from .models import Topic, Listening, Reading, NewWords, Speaking, OldWords
# Register your models here.

class topic_admin(admin.ModelAdmin):
    list_display = ('id', 'Chude')

admin.site.register(Topic, topic_admin)
admin.site.register(Listening)
admin.site.register(Reading)
admin.site.register(NewWords)
admin.site.register(Speaking)
admin.site.register(OldWords)

from django.contrib import admin
from .models import Topic, AccessRecord, WebPage, User_Info
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(User_Info)
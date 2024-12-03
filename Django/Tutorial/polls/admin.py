from django.contrib import admin

# Register your models here.

from .models import Question, Choice, User

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)

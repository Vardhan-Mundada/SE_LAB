from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Qcategory)

class QuestionAdmin(admin.ModelAdmin):
    list_display=['question', 'level']
admin.site.register(models.Question, QuestionAdmin)
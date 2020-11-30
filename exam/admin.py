from django.contrib import admin
from .models import FileUpload,Question
from studentdetails.models import Result
# Register your models here.
admin.site.register(FileUpload)
admin.site.register(Question)
admin.site.register(Result)

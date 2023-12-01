from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Question)
admin.site.register(Userdetail)
admin.site.register(Docfile)
admin.site.register(Excelfile)
admin.site.register(Pdffile)
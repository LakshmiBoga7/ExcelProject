from django.contrib import admin
from .models import Myexcel
from import_export.admin import ImportExportModelAdmin

@admin.register(Myexcel)
class MyexcelAdmin(ImportExportModelAdmin):
    pass
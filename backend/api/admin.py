from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Contests)
class ContestAdmin(admin.ModelAdmin):
    list_display = ['id','Place','Name_Of_Contest']
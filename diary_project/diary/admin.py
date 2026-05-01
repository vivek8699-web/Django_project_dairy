from django.contrib import admin
from .models import DiaryEntry

# Register your models here.
@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "user", "created_at")
    list_filter = ("date", "user")
    search_fields = ("title", "content")

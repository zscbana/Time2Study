from django.contrib import admin
from .models import StudySession

class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'duration', 'created_at')  # Fields to display in the list view
    search_fields = ('user__username',)  # Enable searching by username

admin.site.register(StudySession, StudySessionAdmin)

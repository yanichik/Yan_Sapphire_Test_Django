from django.contrib import admin

from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'rating', 'created_at', 'updated_at']
    list_filter = ['author', 'created_at', 'updated_at']
    search_fields = ['author', 'created_at', 'updated_at']


admin.site.register(Submission, SubmissionAdmin)

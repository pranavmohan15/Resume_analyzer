from django.contrib import admin
from .models import Resume, Job, MatchResult


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'user')
    search_fields = ('position', 'company')
    list_filter = ('company',)


@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ('resume', 'job', 'match_score')
    list_filter = ('match_score',)
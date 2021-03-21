from django.contrib import admin

from resumeapp.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created', 'published')
    list_filter = ('is_draft',)

    def published(self, obj):
        return not Resume.objects.filter(user__resume=obj).first().is_draft

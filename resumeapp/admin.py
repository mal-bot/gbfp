from django.contrib import admin

from resumeapp.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created', 'published')
    list_display_links = ('user', 'name')
    list_filter = ('is_draft',)

    def published(self, obj):
        return not Resume.objects.filter(user__resume=obj).first().is_draft
    published.short_description = 'Опубликовано'
    published.boolean = True

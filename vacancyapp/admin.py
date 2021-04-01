from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from vacancyapp.models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'published', 'is_approved')
    list_display_links = ('name', 'company')
    list_filter = ('is_approved',)

    def published(self, obj):
        return not Vacancy.objects.filter(company__vacancy=obj).first().draft
    published.short_description = 'Опубликовано'
    published.boolean = True


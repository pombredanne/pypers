from django.contrib import admin
from papers.models import Tag, Paper


class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    actions = None


class PaperAdmin(admin.ModelAdmin):
    ordering = ('-year',)
    actions = None
    list_display = ('year', 'authors', 'title')
    list_filter = ('tags', 'rating')


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Paper, PaperAdmin)

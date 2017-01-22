from django.contrib import admin
from django.template.defaultfilters import truncatechars
from papers.models import Tag, Paper


class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    actions = None


class PaperAdmin(admin.ModelAdmin):
    ordering = ('-year',)
    actions = None
    list_display = ('year', 'authors', 'title_short', 'rating_stars',
                    'tags_list', 'citekey')
    list_display_links = ('title_short',)
    list_filter = ('tags', 'rating', 'read_status')
    search_fields = ('full_authors', 'title', 'year')

    def title_short(self, obj):
        return truncatechars(obj.title, 48)
    title_short.short_description = 'title'

    def rating_stars(self, obj):
        return '★' * (obj.rating or 0)
    rating_stars.short_description = 'rating'

    def tags_list(self, obj):
        return ', '.join(sorted(t.name for t in obj.tags.all()))
    tags_list.short_description = 'tags'


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Paper, PaperAdmin)

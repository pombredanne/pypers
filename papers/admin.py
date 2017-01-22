# import os.path as op
from django.contrib import admin
# from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from papers.models import Tag, Paper


class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)
    actions = None


class RatingFilter(admin.SimpleListFilter):
    title = 'Rating'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [(str(i), '★' * i) for i in range(1, 6)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(rating__gte=self.value())
        else:
            return queryset


class PaperAdmin(admin.ModelAdmin):
    ordering = ('-year',)
    actions = None
    readonly_fields = ('id',)
    list_display = ('year', 'authors', 'title_short', 'rating_stars',
                    'tags_list', 'citekey', 'imported_date', 'has_notes')
    list_display_links = ('authors',)
    list_filter = (RatingFilter,
                  'tags',
                   'read_status')
    search_fields = ('full_authors', 'title', 'year',
                     'summary', 'annotations')

    def notes_html(self, obj):
        if not obj.notes:
            return ''
        return format_html(obj.notes.strip().replace('\n', '<br />'))
    notes_html.short_description = 'notes'

    def has_notes(self, obj):
        return obj.notes is not None
    has_notes.boolean = True

    def title_short(self, obj):
        s = truncatechars(obj.title, 64)
        if not obj.pdf_path:
            return s
        path = reverse('get_paper')
        return format_html('<a href="%s?paper_id=%d" target="_blank">%s</a>' %
                           (path, obj.id, s))
    title_short.short_description = 'title'

    def rating_stars(self, obj):
        return '★' * (obj.rating or 0)
    rating_stars.short_description = 'rating'

    def tags_list(self, obj):
        return ', '.join(sorted(t.name for t in obj.tags.all()))
    tags_list.short_description = 'tags'

    class Media:
        css = {
             'all': ('css/admin/styles.css',)
        }


# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Paper, PaperAdmin)

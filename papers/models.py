from django.db import models


class Tag(models.Model):
    name = models.CharField('name', max_length=128)

    def __str__(self):
        return self.name


class Paper(models.Model):
    full_authors = models.CharField('authors', max_length=512)
    authors = models.CharField('authors', max_length=128)
    title = models.CharField('title', max_length=256)
    year = models.PositiveSmallIntegerField('year', blank=True, null=True)
    citekey = models.CharField('citekey', max_length=16, unique=True)
    rating = models.PositiveSmallIntegerField('rating', blank=True, null=True)
    notes = models.TextField('notes', null=True)
    read_status = models.BooleanField('read_status')
    imported_date = models.DateField('imported_date', blank=True, null=True)
    pdf_path = models.CharField('pdf_path', max_length=128,
                                blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def has_notes(self):
        return self.notes != ''

    def __str__(self):
        return '%d %s - %s' % (self.year, self.authors, self.title)

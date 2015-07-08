from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Count(models.Model):
    total_shelves = models.IntegerField()
    total_books = models.IntegerField(null = True,blank = True)
    
    def __unicode__(self):
        return str(self.total_shelves)
    
    
class Shelf(models.Model):
    shelf_no = models.IntegerField(primary_key = True)
    row_1 = models.IntegerField(default = 0)
    row_2 = models.IntegerField(default = 0)
    row_3 = models.IntegerField(default = 0)
    book_file = models.FileField()

    class Meta:
        ordering = ['shelf_no']

    def get_absolute_url(self):
        return reverse('shelf_detail', kwargs = {'pk':self.pk})

    def __unicode__(self):
        return unicode(self.shelf_no)
 
class Book(models.Model):
    accession_no = models.CharField(max_length = 6)
    shelf = models.ForeignKey(Shelf)
    # appx_row = models.ForeignKey(Row)
    
    def __unicode__(self):
        return self.accession_no
    
class TagError(models.Model):
    ERROR_TYPES = (
        ('W','Weak Tag'),
        ('N','No Tag'),
        ('M','Multiple Tags'),
        ('O','Other')
    )
    book = models.ForeignKey(Book)
    error_type = models.CharField(max_length = 1, choices = ERROR_TYPES)
    corrected = models.BooleanField(default = 'FALSE')

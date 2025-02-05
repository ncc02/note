from django.db import models
from ckeditor.fields import RichTextField

class Note(models.Model):
    content = RichTextField()

    def __str__(self):
        return "Sticky Note"

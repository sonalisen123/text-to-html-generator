

from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class Text(models.Model):
    textarea = RichTextField(blank=True,null=True)
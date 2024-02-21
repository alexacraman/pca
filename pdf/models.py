from django.db import models
from django.urls import reverse

class PDFDocument(models.Model):
    title    = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/')
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('pdf:open-pdf', kwargs={'pk': self.pk})

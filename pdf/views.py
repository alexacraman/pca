from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.http import FileResponse
from django.conf import settings
from django.views import View
from django.shortcuts import get_object_or_404
from .models import PDFDocument


class PDFUploadView(CreateView):
    model = PDFDocument
    template_name = 'pdf/pdf_upload.html'
    fields = ['title', 'pdf_file']
    success_url = reverse_lazy('pdf:list-pdf')

class PDFListView(ListView):
    model = PDFDocument
    template_name = 'pdf/pdf_list.html'
    context_object_name = 'pdf_documents'
    ordering = '-updated'


class OpenPDFView(View):
    def get(self, request, pk):
        pdf_doc  = get_object_or_404(PDFDocument, pk=pk)
        pdf_file = open(pdf_doc.pdf_file.path, 'rb')
        response = FileResponse(pdf_file, content_type='application/pdf')
        return response


class PDFDownloadView(DetailView):
    model = PDFDocument
    template_name = 'pdf/pdf_download.html'


class PDFUpdateView(UpdateView):
    model = PDFDocument
    fields = ['title', 'pdf_file']
    template_name = 'pdf/pdf_upload.html'
    context_object_name = 'pdf_documents'
    success_url = reverse_lazy('pdf:list-pdf')

class PDFDeleteView(DeleteView):
    model = PDFDocument
    template_name = 'pdf/delete.html'
    context_object_name = 'pdf_documents'
    success_url = reverse_lazy('pdf:list-pdf')
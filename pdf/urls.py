from django.urls import path
from . import views

app_name = 'pdf' 

urlpatterns = [
    path('upload/', views.PDFUploadView.as_view(), name='upload-pdf'),
    path('pdfs/', views.PDFListView.as_view(), name='list-pdf'),
    path('pdfs/<int:pk>', views.OpenPDFView.as_view(), name='open-pdf'),
    path('download/<int:pk>/', views.PDFDownloadView.as_view(), name='download-pdf'),
    path('download/<int:pk>/delete/', views.PDFDeleteView.as_view(), name='delete-pdf'),
    path('download/<int:pk>/update/', views.PDFUpdateView.as_view(), name='update-pdf'),
]
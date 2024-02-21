from django.shortcuts import render, get_object_or_404


def home_page(request):
    return render(request, 'landing/home_page.html', {})

def about_page(request):
    return render(request, 'landing/about_page.html', {})

def pca_does(request):
    return render(request, 'landing/pca_does.html', {})

def pca_member(request):
    return render(request, 'landing/pca_member.html', {})

def meet_team(request):
    return render(request, 'landing/meet-team.html',{})


def consortium_uk(request):
    return render(request, 'landing/consortium.html', {})


from events.models import Event
from accounts.models import CommitteeMembers
from venues.models import Venue
from pdf.models import PDFDocument
from django.db.models import Q

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        event_results = Event.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
            ).distinct()
        member_results = CommitteeMembers.objects.filter(
            Q(description__icontains=query)
        ).distinct()
        venue_results = Venue.objects.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
        ).distinct()
        pdf_results = PDFDocument.objects.filter(
            Q(title__icontains=query)
        ).distinct()
        combined_results = list(event_results)+list(member_results)+list(venue_results)+list(pdf_results)
        print(combined_results)
        return render(request, 'landing/search_results.html', {'combined_results': combined_results, 'query': query})

        




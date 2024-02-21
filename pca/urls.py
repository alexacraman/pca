from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from .views import home_page, about_page, pca_does, pca_member, meet_team, consortium_uk, search_view

urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about_page, name='about_page'),
    path('what-the-pca-does/', pca_does, name='pca_does'),
    path('membership/', pca_member, name='pca_member'),
    path('committee-members/', meet_team, name='committee-members'),
    path('consortium/', consortium_uk, name='consortium'),
    path('search/results/', search_view, name='search_view'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('pdf/', include('pdf.urls', namespace='pdf')),
    path('venues/', include('venues.urls', namespace='venues')),
    path('membership/', include('membership.urls', namespace='membership')),
    path('events/', include('events.urls', namespace='events')),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('account/', include('accounts.urls', namespace='account')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

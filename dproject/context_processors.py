from django.contrib.sites.models import Site
from django.contrib.flatpages.models import FlatPage



def site_processor(request):
    return {'site': Site.objects.get_current()}

def flatpages_links(request):
    # Récupérer les flatpages publiées pour le site actuel
    current_site = Site.objects.get_current()
    flatpages = FlatPage.objects.filter(sites=current_site).values('url', 'title')
    return {'flatpages_links': flatpages}

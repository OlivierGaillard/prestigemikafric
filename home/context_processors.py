# monapp/context_processors.py
from django.urls import reverse

def apps_links(request):
    apps = [
        {"name": "Accueil", "url": reverse("home:home")},
        {"name": "Atelier", "url": reverse("atelier:index")},
        # Ajoutez vos autres apps ici
    ]
    return {"apps_links": apps}

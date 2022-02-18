from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# Startseite
def index(request):
    if request.method == "GET":
        # beim betreten der Website
        return render(request, "groupmanager/index.html")

    elif request.method == "POST":
        # wenn auf den "Event beitreten" Button geklickt wird
        event_id = request.POST["event_id"]
        if event_id.strip() is None:
            # wenn keine event ID angegeben wurde
            return render(request, "groupmanager/index.html", {"error_message": "Das Feld ist leer"})
        else:
            return HttpResponse(f"Betrete Event {event_id}")
    else:
        raise Http404()

def new(request):
    return HttpResponse("yeet")
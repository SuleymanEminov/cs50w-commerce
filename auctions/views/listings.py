from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(active = True)
    })
    


def listing_view(request, id):
    """
            
    """
    try:
        listing = Listing.objects.get(pk=id)
    except Listing.DoesNotExist:
        messages.add_message(request, messages.ERROR, "This is not available") 
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'auctions/listing_view.html', {
            "listing": Listing.objects.get(pk=id)
    })

@login_required
def listing_bidding(request):
    current_user = request.user
    if request.bidder_id == current_user:
        False
    pass
    
    
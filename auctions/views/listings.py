from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..models import User, Listing


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(active = True)
    })
    


def listing_view(request):
    # current_user = request.user
    # listing create
    # listing.name = "xxxx"
    # listing.price = 1235
    # listing.user = current_user
    pass

def listing_bidding(request):
    current_user = request.user
    if request.bidder_id == current_user:
        False
    pass
    
    
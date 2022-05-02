from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import User
from ..forms import *

@login_required
def add_to_watchlist(request, id):
    """add listing to user's watchlist"""
    if request.method == "POST":
        listing = Listing.objects.get(id=id)
        watchlist = request.user.watchlist
        if listing in watchlist.all():
            watchlist.remove(listing)
        else:
            watchlist.add(listing)

    url = reverse('listing_view', kwargs={'id': id})
    return HttpResponseRedirect(url)

@login_required
def watchlist(request):
    '''display watchlist'''
    return render(request, "auctions/index.html", {
        "listings" : request.user.watchlist.all(),
        "title" : "Watchlist"
    })

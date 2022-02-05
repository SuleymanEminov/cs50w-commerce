from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ...models import User


def index(request):
    return render(request, "auctions/index.html")


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
    
    
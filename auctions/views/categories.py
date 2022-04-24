from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..models import User, Listing, Category

def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": Category.objects.all()
    })

def category_listings(request, category):
    """
        Show all listings of a certain category
    """
    cat = Category.objects.filter(name=category).first()
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(category=cat)
    })
    
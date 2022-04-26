from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..models import User, Listing, CATEGORIES

def simplify_categories_list():
    unique_list = [ele[0] for ele in CATEGORIES]
    return unique_list

def categories(request):
    """ display list of categories """
    categories = simplify_categories_list()


    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category_listings(request, category):
    """
        Show all listings of a certain category
    """
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(category=category)
    })
    
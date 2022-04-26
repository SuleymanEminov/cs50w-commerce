from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import User
from ..forms import *

@login_required
def create_listing(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = user
            listing.active = True
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'auctions/create_listing.html', {
                "form": form
            })
    else:
        return render(request, 'auctions/create_listing.html', {
            'form': ListingForm()
        })
    
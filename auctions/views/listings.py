from multiprocessing import context
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import User, Listing, Bid
from ..forms import CommentForm, BiddingForm



def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all().filter(active = True)
    })
    


def listing_view(request, id):
    """
        View page of a specific listing  
    """
    template_name = 'listing_view.html'
    context = {}
    
    # check listing exists
    try:
        listing = get_object_or_404(Listing,id=id)
    except Listing.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Entry does not exist") 
        return HttpResponseRedirect(reverse("index"))
    
    # add context to display on listing view
    context["listing"] = listing
    context['comments'] = listing.comments.all().filter(active=True)
    context["comment_form"] = CommentForm()
    context["bidding_form"] = BiddingForm(request.POST or None)
    # context['bidding_error'] = bidding_error
    
    return render(request, 'auctions/listing_view.html',context)

@login_required
def listing_bidding(request, id):
    current_user = request.user
    bidding_form = BiddingForm(request.POST or None)
    bidding_error = False #defualt is False
    
    if bidding_form.is_valid():
        listing = Listing.objects.get(id=id)
        new_bid = bidding_form.save(commit=False)
        current_bids = Bid.objects.filter(listing=listing)
        is_highest_bid = all(new_bid.amount > n.amount for n in current_bids)
        is_valid_first_bid = new_bid.amount >= listing.price

        if is_highest_bid and is_valid_first_bid:
            new_bid.listing = listing
            new_bid.user = current_user
            new_bid.save()
        else:
            # add context to display on listing view
            context = {}
            context["listing"] = listing
            context['comments'] = listing.comments.all().filter(active=True)
            context["comment_form"] = CommentForm()
            context["bidding_form"] = BiddingForm(request.POST or None)
            context["message"] = "Bid higher."
            return render(request, "auctions/listing_view.html", context)         
    url = reverse("listing_view", kwargs={'id':id})
    return HttpResponseRedirect(url)
    
    
@login_required
def close_auction(request,id):
    listing = Listing.objects.get(id=id)
    if request.user == listing.user:
        listing.active = False
        listing.save()

    url = reverse("listing_view", kwargs={'id':id})
    return HttpResponseRedirect(url)
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import User, Listing
from ..forms import CommentForm



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
    
    return render(request, 'auctions/listing_view.html',context)

@login_required
def listing_bidding(request):
    current_user = request.user
    if request.bidder_id == current_user:
        False
    pass
    
    
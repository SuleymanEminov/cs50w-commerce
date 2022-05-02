from django.http import HttpResponseRedirect
from django.urls import reverse
from ..models import Listing,User
from ..forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def post_comment(request,id):
    template_name = 'listing_view.html'
    listing = get_object_or_404(Listing, id=id)
    comments = listing.comments.filter(active=True)
    new_comment = None
    # Comment Posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        user = User.objects.get(username=request.user)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.listing = listing
            new_comment.user = user
            # Save the comment to the database
            new_comment.save()
        
        else:
            comment_form = CommentForm()

        url = reverse('listing_view',kwargs={'id':id})
        return HttpResponseRedirect(url)

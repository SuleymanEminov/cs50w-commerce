from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import User
from ..forms import *

def watchlist(request):
    # add listing to user's watchlist
    pass

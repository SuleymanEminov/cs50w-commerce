from django.urls import path

from . import views

from django.conf import *
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.category_listings, name="category_listings"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing_view/<str:id>", views.listing_view, name="listing_view"),
    path("add_to_watchlist/<str:id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("post_comment/<str:id>", views.post_comment, name="post_comment"),
    path("listing_bidding/<str:id>", views.listing_bidding, name="listing_bidding"),
    path("close_auction/<str:id>", views.close_auction, name="close_auction"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

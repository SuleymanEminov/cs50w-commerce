from django.urls import path
from .views.authenticate import authenticate


urlpatterns = [
    path("", authenticate.index, name="index"),
    path("login", authenticate.login_view, name="login"),
    path("logout", authenticate.logout_view, name="logout"),
    path("register", authenticate.register, name="register")
]

from django.urls import path
from . import views

urlpatterns =  [
    path("", views.index, name='index'),
    path("about", views.about, name="about"),
    path("formulaire", views.form, name="formulaire"),
    path("register", views.register, name="register"),
    path("login", views.connexion, name="login"),
    path("accueil", views.accueil, name="accueil"),
    path("logout", views.deconnexion, name="logout"),
    path("chatroom", views.chatroom, name="chatroom"),
]
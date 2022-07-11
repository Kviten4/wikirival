from django.urls import path
from . import views

app_name ="encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("createnewpage", views.crnewpage, name="crnewpage"),
    path("random", views.randompage, name="randompage"),
    path("<str:title>", views.article, name="article"),
    path("search/", views.search, name="search"),
    path("edit/", views.editarticle, name="editarticle")
]

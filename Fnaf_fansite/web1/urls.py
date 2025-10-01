
from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home, name="home"),
    path("foro/", core_views.foro, name="foro"),
    path("gallery/", core_views.gallery, name="gallery"),
    path("quest/", core_views.quest, name="quest"),
    path("personajes/", core_views.personajes, name="personajes"),
]
from django.urls import path
from . import views


app_name = "tracker"

urlpatterns = [
    path("", views.index, name="home"),
    path(
        "applications/",
        views.application_list,
        name="application_list",
    ),

    path("applications/<int:pk>/edit/", views.edit, name="edit"),
    path("applications/<int:pk>/delete/", views.delete, name="delete"),
]

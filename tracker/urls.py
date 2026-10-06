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
]

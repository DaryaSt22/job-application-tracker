from django.shortcuts import render
from django.http import HttpResponse
from .models import JobApplication

def index(request):
    return render(request, "tracker/index.html")

def application_list(request):
    applications = JobApplication.objects.all()
    return render(
        request,
        "tracker/application_list.html",
        {"applications": applications},
    )

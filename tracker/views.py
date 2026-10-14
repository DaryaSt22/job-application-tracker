from django.shortcuts import render
from .models import JobApplication
from .forms import JobApplicationForm


def index(request):
    return render(request, "tracker/index.html")

def application_list(request):
    applications = JobApplication.objects.all()
    form = JobApplicationForm()
    return render(
        request,
        "tracker/application_list.html",
        {"applications": applications, "form": form},
    )

def edit(request, pk):
    application = JobApplication.objects.get(pk=pk)
    form = JobApplicationForm(instance=application)
    return render(
        request,
        "tracker/edit.html",
        {"edit": application, "form": form},
    )

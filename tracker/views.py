from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm


def index(request):
    return render(request, "tracker/index.html")


def application_list(request):
    applications = JobApplication.objects.all()
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker:application_list")
    else:
        form = JobApplicationForm()
    return render(
        request,
        "tracker/application_list.html",
        {"applications": applications, "form": form},
    )



def edit(request, pk):
    application = JobApplication.objects.get(pk=pk)
    form = JobApplicationForm(instance=application)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        is_form_valid = form.is_valid()
        if is_form_valid:
            form.save()
            return redirect("tracker:application_list")
    return render(
        request,
        "tracker/edit.html",
        {"edit": application, "form": form},
    )

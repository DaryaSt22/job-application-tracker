from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


def index(request):
    return render(request, "tracker/index.html")

def application_list(request):
    applications = JobApplication.objects.all()
    total_applications = applications.count()
    selected_status = request.GET.get("status")
    search_query = request.GET.get("q")
    status_choices = JobApplication.Status.choices
    if selected_status:
        applications = applications.filter(status=selected_status)

    if search_query:
        applications = applications.filter(company__icontains=search_query)

    applications = applications.order_by("-applied_on")

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
        {"applications": applications, "form": form, "status_choices": status_choices, "total_applications": total_applications},
    )

def edit(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
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
        {"application": application, "form": form},
    )

def delete(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        application.delete()
        return redirect("tracker:application_list")

    return render(
        request,
        "tracker/delete.html",
        {"application": application},
    )

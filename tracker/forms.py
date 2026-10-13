from django import forms

from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "company",
            "job_title",
            "vacancy_url",
            "status",
            "applied_on",
            "interview_at",
            "notes",
        ]

        widgets = {

            "applied_on": forms.DateInput(attrs={"type": "date"}),
            "interview_at": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "status": forms.Select(),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }

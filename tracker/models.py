from django.db import models
from django.utils import timezone

class JobApplication(models.Model):
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    vacancy_url = models.URLField(max_length=200)
    status = models.CharField(max_length=200)
    applied_on = models.DateField(default=timezone.localdate)
    interview_at = models.DateTimeField(null=True, blank=True)
    notification = models.CharField(max_length=200)

from django.db import models

class JobApplication(models.Model):
    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    vacancy_url = models.URLField(max_length=200)

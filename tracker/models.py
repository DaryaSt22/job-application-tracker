from django.db import models
from django.utils import timezone

class JobApplication(models.Model):
    class Status(models.TextChoices):
        SENT = "sent", "Отклик отправлен"
        VIEWED = "viewed", "Отклик просмотрен"
        APPROVED = "approved"
        DECLINED = "declined", "Отказ"
        CONTACTED = "contacted", "Работодатель связался"
        INTERVIEW = "interview", "Собеседование назначено"
        OFFER = "offer", "Оффер получен"

    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    vacancy_url = models.URLField(max_length=200)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.SENT)
    applied_on = models.DateField(default=timezone.localdate)
    interview_at = models.DateTimeField(null=True, blank=True)
    notification = models.CharField(max_length=200)

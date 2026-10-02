from django.db import models
from django.utils import timezone

class JobApplication(models.Model):
    class Status(models.TextChoices):
        SENT = "sent", "Отклик отправлен"
        VIEWED = "viewed", "Отклик просмотрен"
        DECLINED = "declined", "Отказ"
        CONTACTED = "contacted", "Работодатель связался"
        INTERVIEW = "interview", "Собеседование назначено"
        OFFER = "offer", "Оффер получен"

    company = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    vacancy_url = models.URLField(max_length=200)
    status = models.CharField(max_length=200, choices=Status.choices, default=Status.SENT)
    applied_on = models.DateField(default=timezone.localdate)
    interview_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} — {self.job_title}"

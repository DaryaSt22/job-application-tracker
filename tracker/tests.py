from django.test import TestCase
from django.urls import reverse
from .models import JobApplication


class JobApplicationViewTests(TestCase):

    def test_edit_missing_application_returns_404(self):
        url = reverse("tracker:edit", kwargs={"pk": 999999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_missing_application_returns_404(self):
        url = reverse("tracker:delete", kwargs={"pk": 999999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_application_list_returns_200(self):
        url = reverse("tracker:application_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/application_list.html")

    def test_create_application(self):
        url = reverse("tracker:application_list")
        data={"company": "Test Company", "job_title": "Python Developer", "status": "sent",
                                    "vacancy_url": "https://www.example.com", "applied_on": "2026-11-28", }
        response = self.client.post(url, data=data)
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(response.status_code, 302)
        application = JobApplication.objects.get()
        self.assertEqual(application.company, "Test Company")

    def test_update_application(self):
        application = JobApplication.objects.create(company='Old Company')
        url = reverse("tracker:edit", kwargs={"pk": application.pk})
        data = {"company": "Updated Company", "job_title": "Python Developer", "status": "sent",
                "vacancy_url": "https://www.example.com", "applied_on": "2026-11-28", }
        response = self.client.post(url, data=data)
        application.refresh_from_db()
        self.assertEqual(application.company, "Updated Company")

    def test_delete_application(self):
        application = JobApplication.objects.create(company='Old Company')
        url = reverse("tracker:delete", kwargs={"pk": application.pk})
        response = self.client.post(url)
        self.assertEqual(JobApplication.objects.count(), 0)
        self.assertEqual(response.status_code, 302)


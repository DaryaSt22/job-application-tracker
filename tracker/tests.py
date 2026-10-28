from django.test import TestCase
from django.urls import reverse


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

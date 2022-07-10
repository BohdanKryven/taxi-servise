from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="12345678",
            license_number="ABC12345"
        )

        self.client.force_login(self.admin_user)

        self.driver = get_user_model().objects.create_user(
            username="user",
            password="12345678",
            license_number="ABC12346"
        )

    def test_driver_license_listed(self):
        """
        Test that 'license_number' is in 'list_display' on admin page
        """
        url = reverse("admin:taxi_driver_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)

    def test_driver_detailed_license_listed(self):
        """
        Test that 'license_number' is in 'list_display' on driver detail page
        """
        url = reverse("admin:taxi_driver_change", args=[self.driver.id])
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)

    def test_driver_add_license_listed(self):
        """
        Test that 'license_number' is in 'list_display' on driver detail page
        """
        url = reverse("admin:taxi_driver_add")
        res = self.client.get(url)

        self.assertContains(res, "License number:")

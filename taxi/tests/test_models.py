from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="BMW", country="Germany")
        self.assertEqual(str(manufacturer), f"{manufacturer.name} {manufacturer.country}")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="admin",
            password="12345678",
            first_name="Bohdan",
            last_name="Kryven",
            license_number="ABC12345"
        )

        self.assertEqual(str(driver), f"{driver.username} ({driver.first_name} {driver.last_name})")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="BMW", country="Germany")
        car = Car.objects.create(model="V1", manufacturer=manufacturer)

        self.assertEqual(str(car), f"Model: {car.model} Manufacturer: {car.manufacturer.name}")

    def test_create_driver_with_license_number(self):
        username = "admin"
        password = "12345678"
        license_number = "ABC12345"

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password), password)
        self.assertEqual(driver.license_number, license_number)


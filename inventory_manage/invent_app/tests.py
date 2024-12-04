from django.test import TestCase
from django.contrib.gis.geos import Point
from invent_app.models import Location, Accommodation, LocalizeAccommodation
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

class LocationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            id="loc1",
            title="Test Country",
            center=Point(0, 0),
            country_code="TC",
            location_type="Country"
        )

    def test_location_creation(self):
        """Test the creation of a Location instance"""
        self.assertEqual(self.location.title, "Test Country")
        self.assertEqual(self.location.country_code, "TC")
        self.assertEqual(self.location.center.coords, (0, 0))
        self.assertEqual(self.location.location_type, "Country")

    def test_location_invalid_creation(self):
        """Test invalid creation of a Location instance"""
        with self.assertRaises(IntegrityError):
            Location.objects.create(
                id="loc2",
                title=None,  # Missing title should fail
                center=Point(1, 1),
                country_code="TC",
                location_type="City"
            )

    def test_location_str(self):
        """Test string representation of Location"""
        self.assertEqual(str(self.location), "Test Country")


class AccommodationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.location = Location.objects.create(
            id="loc1",
            title="Test Country",
            center=Point(0, 0),
            country_code="TC",
            location_type="Country"
        )
        self.accommodation = Accommodation.objects.create(
            id="acc1",
            title="Test Accommodation",
            country_code="TC",
            bedroom_count=3,
            usd_rate=100.0,
            location=self.location,
            user=self.user,
            published=True
        )

    def test_accommodation_creation(self):
        """Test the creation of an Accommodation instance"""
        self.assertEqual(self.accommodation.title, "Test Accommodation")
        self.assertEqual(self.accommodation.bedroom_count, 3)
        self.assertEqual(self.accommodation.usd_rate, 100.0)
        self.assertEqual(self.accommodation.user.username, "testuser")
        self.assertTrue(self.accommodation.published)

    def test_accommodation_invalid_creation(self):
        """Test invalid creation of an Accommodation instance"""
        with self.assertRaises(IntegrityError):
            Accommodation.objects.create(
                id="acc2",
                title=None,  # Missing title should fail
                country_code="TC",
                bedroom_count=2,
                usd_rate=200.0,
                location=self.location,
                user=self.user,
                published=True
            )

    def test_accommodation_str(self):
        """Test string representation of Accommodation"""
        self.assertEqual(str(self.accommodation), "Test Accommodation")


class LocalizeAccommodationModelTest(TestCase):
    def setUp(self):
        # Create an Accommodation instance for the LocalizeAccommodation relationship
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.location = Location.objects.create(
            id="loc1",
            title="Test Country",
            center=Point(0, 0),
            country_code="TC",
            location_type="Country"
        )
        self.accommodation = Accommodation.objects.create(
            id="acc1",
            title="Test Accommodation",
            country_code="TC",
            bedroom_count=3,
            usd_rate=100.0,
            location=self.location,
            user=self.user,
            published=True
        )

        self.localized_accommodation = LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language="en",
            description="A cozy place to stay.",
            policy={"check_in": "2 PM", "check_out": "11 AM"}
        )

    def test_localized_accommodation_creation(self):
        """Test the creation of LocalizeAccommodation instance"""
        self.assertEqual(self.localized_accommodation.language, "en")
        self.assertEqual(self.localized_accommodation.description, "A cozy place to stay.")
        self.assertEqual(self.localized_accommodation.policy["check_in"], "2 PM")
        self.assertEqual(self.localized_accommodation.property, self.accommodation)

    def test_localized_accommodation_invalid_creation(self):
        """Test invalid creation of LocalizeAccommodation instances"""
        with self.assertRaises(IntegrityError):
            LocalizeAccommodation.objects.create(
                property=self.accommodation,
                language=None,  # Missing language should fail
                description="A description",
                policy={"check_in": "2 PM"}
            )

    def test_localized_accommodation_str(self):
        """Test string representation of LocalizeAccommodation"""
        self.assertEqual(
            str(self.localized_accommodation),
            f"{self.localized_accommodation.property.title} - {self.localized_accommodation.language}"
        )

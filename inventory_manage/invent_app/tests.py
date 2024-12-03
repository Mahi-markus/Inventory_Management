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
        self.assertEqual(self.location.title, "Test Country")
        self.assertEqual(self.location.country_code, "TC")
        self.assertEqual(self.location.center.coords, (0, 0))
        self.assertEqual(self.location.location_type, "Country")

    def test_location_invalid_creation(self):
        with self.assertRaises(IntegrityError):
            Location.objects.create(
                id="loc2",
                title=None,  # Missing title should fail
                center=Point(1, 1),
                country_code="TC",
                location_type="City"
            )

    def test_location_str(self):
        self.assertEqual(str(self.location), "Test Country")

class AccommodationModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Create a location with a center point
        self.location = Location.objects.create(
            id="loc1",
            title="Test Country",
            center=Point(0, 0),  # Correctly setting the center as Point
            country_code="TC",
            location_type="Country"
        )
        
        # Create an accommodation with a valid center point
        self.accommodation = Accommodation.objects.create(
            id="acc1",
            title="Test Accommodation",
            country_code="TC",
            bedroom_count=3,
            usd_rate=100.0,
            location=self.location,
            user=self.user,
            center=Point(1, 1)  # Adding a center point for the accommodation
        )

    def test_accommodation_creation(self):
        self.assertEqual(self.accommodation.title, "Test Accommodation")
        self.assertEqual(self.accommodation.bedroom_count, 3)
        self.assertEqual(self.accommodation.usd_rate, 100.0)
        self.assertEqual(self.accommodation.user.username, "testuser")
        self.assertEqual(self.accommodation.center.coords, (1, 1))  # Test the center value

    def test_accommodation_invalid_creation(self):
        with self.assertRaises(IntegrityError):
            Accommodation.objects.create(
                id="acc2",
                title=None,  # Missing title should fail
                country_code="TC",
                bedroom_count=2,
                usd_rate=200.0,
                location=self.location,
                user=self.user,
                center=None  # Missing center should fail as well
            )

    def test_accommodation_str(self):
        self.assertEqual(str(self.accommodation), "Test Accommodation")


class LocalizeAccommodationModelTest(TestCase):
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
            user=self.user
        )
        self.localized_accommodation = LocalizeAccommodation.objects.create(
            accommodation=self.accommodation,
            language="en",
            localized_title="Localized Test Accommodation",
        )

    def test_localized_accommodation_creation(self):
        self.assertEqual(self.localized_accommodation.language, "en")
        self.assertEqual(self.localized_accommodation.localized_title, "Localized Test Accommodation")
        self.assertEqual(self.localized_accommodation.accommodation.title, "Test Accommodation")

    def test_localized_accommodation_invalid(self):
        with self.assertRaises(IntegrityError):
            LocalizeAccommodation.objects.create(
                accommodation=None,  # Missing accommodation should fail
                language="fr",
                localized_title="Titre localisé"
            )

    def test_localized_accommodation_str(self):
        self.assertEqual(
            str(self.localized_accommodation),
            f"Localized Test Accommodation ({self.localized_accommodation.language})"
        )



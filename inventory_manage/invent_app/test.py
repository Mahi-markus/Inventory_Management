from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Location, Accommodation, LocalizeAccommodation

class LocationModelTest(TestCase):
    def test_location_creation_invalid_data(self):
        """
        This test will fail because 'id' is required and it's missing.
        """
        location = Location.objects.create(
            title="Test Location",  # Missing required 'id'
            location_type="City",
            country_code="BD",
        )
        self.assertEqual(location.title, "Test Location")
        self.assertEqual(location.country_code, "BD")
        self.assertIsNone(location.state_abbr)  # Since we didn't set it
        self.assertIsNone(location.city)  # Since we didn't set it
        self.assertEqual(location.id, "default_id")  # This will fail because 'id' is not set properly.

    def test_location_str(self):
        """
        This test will fail because the string representation assumes a non-existent Location.
        """
        location = Location.objects.create(
            id="12345",
            title="Test Location",
            location_type="City",
            country_code="BD",
        )
        self.assertEqual(str(location), "Nonexistent Location")  # Fails because the location's title is "Test Location" not "Nonexistent Location"


class AccommodationModelTest(TestCase):
    def setUp(self):
        """
        Create a test user and a test location for accommodations.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.location = Location.objects.create(
            id="12345",
            title="Test Location",
            location_type="City",
            country_code="BD",
        )

    def test_accommodation_creation_invalid_data(self):
        """
        This test will fail because 'usd_rate' cannot be negative.
        """
        accommodation = Accommodation.objects.create(
            id="accom001",
            feed=1,
            title="Test Accommodation",
            country_code="BD",
            bedroom_count=2,
            review_score=4.5,
            usd_rate=-100.0,  # Invalid value, usd_rate should not be negative
            center='POINT(1 1)',  # Sample point for the center
            location=self.location,
            user=self.user,
            published=True,
        )
        self.assertEqual(accommodation.title, "Test Accommodation")
        self.assertEqual(accommodation.usd_rate, -100.0)  # This will fail because usd_rate cannot be negative.

    def test_accommodation_str(self):
        """
        This test will fail because the expected title is wrong.
        """
        accommodation = Accommodation.objects.create(
            id="accom001",
            feed=1,
            title="Test Accommodation",
            country_code="BD",
            bedroom_count=2,
            review_score=4.5,
            usd_rate=100.0,
            center='POINT(1 1)',  # Sample point for the center
            location=self.location,
            user=self.user,
            published=True,
        )
        self.assertEqual(str(accommodation), "Wrong Title")  # Fails because the title is "Test Accommodation" not "Wrong Title"


class LocalizeAccommodationModelTest(TestCase):
    def setUp(self):
        """
        Create a test accommodation instance for localization.
        """
        self.user = User.objects.create_user(username='testuser', password='password')
        self.location = Location.objects.create(
            id="12345",
            title="Test Location",
            location_type="City",
            country_code="BD",
        )
        self.accommodation = Accommodation.objects.create(
            id="accom001",
            feed=1,
            title="Test Accommodation",
            country_code="BD",
            bedroom_count=2,
            review_score=4.5,
            usd_rate=100.0,
            center='POINT(1 1)',  # Sample point for the center
            location=self.location,
            user=self.user,
            published=True,
        )

    def test_localize_accommodation_creation_invalid_data(self):
        """
        This test will fail because the language is too long (more than 2 characters).
        """
        localize = LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language="eng",  # Invalid language code; should be 2 characters
            description="Test description in English",
            policy={"cancellation": "no refund"}
        )
        self.assertEqual(localize.language, "eng")  # This will fail as 'eng' is not a valid 2-character language code.

    def test_localize_accommodation_str(self):
        """
        This test will fail because the expected string representation is incorrect.
        """
        localize = LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language="en",
            description="Test description in English",
            policy={"cancellation": "no refund"}
        )
        self.assertEqual(str(localize), "Test Accommodation - fr")  # Fails because the language is 'en' not 'fr'

    def test_localize_accommodation_unique_constraint(self):
        """
        This test will fail because we are testing a scenario that should raise an IntegrityError, 
        but the data provided violates the assumption of uniqueness.
        """
        LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language="en",
            description="First description in English",
            policy={"cancellation": "no refund"}
        )
        localize_duplicate = LocalizeAccommodation.objects.create(
            property=self.accommodation,
            language="en",  # Same language for the same property should raise an error
            description="Second description in English",
            policy={"cancellation": "no refund"}
        )
        self.assertIsNotNone(localize_duplicate)  # This will fail because the model should enforce unique constraint for (property, language).





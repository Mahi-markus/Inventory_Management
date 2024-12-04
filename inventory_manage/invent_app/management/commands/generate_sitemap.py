import json
from django.core.management.base import BaseCommand
from invent_app.models import Location
from django.utils.text import slugify  # Import slugify directly from Django

class Command(BaseCommand):
    help = "Generate a sitemap.json file for all country locations."

    def handle(self, *args, **kwargs):
        # Query all top-level locations (countries)
        countries = Location.objects.filter(parent__isnull=True).order_by('title')

        sitemap = []

        for country in countries:
            # Generate slug for the country
            country_slug = slugify(country.title)
            country_data = {
                country.title: country_slug,  # e.g., "USA": "usa",
                "locations": []              # List of child locations (states/cities)
            }

            # Query child locations (states/cities) of the country
            child_locations = Location.objects.filter(parent=country).order_by('title')
            for child in child_locations:
                # Generate slug for child location (state/city)
                child_slug = f"{country_slug}/{slugify(child.title)}"  # e.g., "usa/florida"
                country_data["locations"].append({
                    child.title: child_slug  # e.g., { "Florida": "usa/florida" }
                })

            sitemap.append(country_data)

        # Save to sitemap.json
        with open('sitemap.json', 'w') as file:
            json.dump(sitemap, file, indent=4)

        self.stdout.write(self.style.SUCCESS('Sitemap generated successfully as sitemap.json'))




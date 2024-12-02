from django.contrib import admin
from .models import  Accommodation, LocalizeAccommodation,Location



# Register Location with custom admin class


# Register Accommodation with custom admin class
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'published', 'created_at','updated_at')
    search_fields = ('title', 'country_code')
    list_filter = ('published',)
   

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'location_type', 'created_at','updated_at')
    search_fields = ('title', 'country_code')
    list_filter = ('location_type',)

# Register LocalizeAccommodation with custom admin class
@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'language')
    search_fields = ('property__title', 'language')
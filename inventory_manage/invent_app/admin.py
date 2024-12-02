from django.contrib import admin

from .models import  Accommodation, LocalizeAccommodation,Location
from leaflet.admin import LeafletGeoAdmin



# Register Location with custom admin class


# Register Accommodation with custom admin class

# Register Accommodation with custom admin class
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country_code', 'bedroom_count', 'published', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code')
    list_filter = ('published',)

    def get_queryset(self, request):
        # Filter accommodations based on the logged-in user
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(user=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        # Automatically set the logged-in user for accommodation creation
        if not obj.pk:  # If it's a new object
            obj.user = request.user
        super().save_model(request, obj, form, change)

   

@admin.register(Location)
class LocationAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'country_code', 'location_type', 'created_at','updated_at')
    search_fields = ('title', 'country_code')
    list_filter = ('location_type',)

# Register LocalizeAccommodation with custom admin class
@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'language')
    search_fields = ('property__title', 'language')

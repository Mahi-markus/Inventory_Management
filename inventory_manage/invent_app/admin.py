from django.contrib import admin

from .models import  Accommodation, LocalizeAccommodation,Location
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from import_export import resources
from import_export.admin import ImportExportModelAdmin





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

    def get_form(self, request, obj=None, **kwargs):
        """
        This method customizes the form to hide the 'user' field for non-superusers.
        """
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            # Hide the 'user' field for non-superusers
            form.base_fields['user'].widget = forms.HiddenInput()
        return form


   
# Define a Resource class for the Location model
class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = ('id', 'title', 'country_code', 'location_type', 'created_at', 'updated_at')  # Include the fields you want to import/export

# Register Location with custom admin class and import/export functionality
@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin, LeafletGeoAdmin):
    list_display = ('id', 'title','country_code', 'location_type', 'created_at', 'updated_at')
    search_fields = ('title', 'country_code')
    list_filter = ('location_type',)

    # Optionally, you can customize the form for importing by using the LocationResource
    resource_class = LocationResource














# Register LocalizeAccommodation with custom admin class
@admin.register(LocalizeAccommodation)
class LocalizeAccommodationAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'language')
    search_fields = ('property__title', 'language')






 # Customize the User Admin form
# Custom User Change Form
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Replace the default User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


from django.urls import path
from . import views
from .views import property_owner_signup

urlpatterns = [
    path('property-owner-signup/', property_owner_signup, name='property_owner_signup'),
    path('login/', property_owner_signup, name='user_login'),
    path('dashboard/', property_owner_signup, name='user_dashboard'),
]

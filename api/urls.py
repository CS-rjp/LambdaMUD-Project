from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('', include('rest_auth.urls')),
    # registration and logins handled here for security and 
    # legal protection both users and developers
    path('registration/', include('rest_auth.registration.urls')),
]

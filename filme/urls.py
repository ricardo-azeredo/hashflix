from django.urls import path, include

#from filme.views import homepage
from .views import homepage

urlpatterns = [
    path('', homepage),
]
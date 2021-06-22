from django.urls import path

from .views import registration_view

app_name = 'adminaccounts'

urlpatterns = [
    path('', registration_view, name='api-register')
]
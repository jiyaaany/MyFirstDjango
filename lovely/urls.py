from django.urls import path
from .views import first, second, third

urlpatterns = [
    path('first/', first),
    path('second/', second),
    path('third/', third),
]
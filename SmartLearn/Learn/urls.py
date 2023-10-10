from django.urls import path
from .views import profile

app_name = 'Learn'

urlpatterns = [
    path('', profile, name='index'),
]

from django.urls import path
from .views import calendar_view, get_events



app_name = 'cabinet'



urlpatterns = [
    path('get_events/', get_events, name='get_events'),
    path('calendar/', calendar_view, name='calendar'),
]

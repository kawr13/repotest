from django.urls import path
from .views import get_events, cabinets_view

app_name = 'cabinet'



urlpatterns = [
    path('get_events/<int:cabinet_id>/', get_events, name='get_events'),
    # path('calendar/', calendar_view, name='calendar'),
    path('cabinets/<int:cab_id>/', cabinets_view, name='cabinet'),
]

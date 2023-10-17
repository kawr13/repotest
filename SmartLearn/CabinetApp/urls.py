from django.urls import path
from .views import get_events, cabinets_view, update_calend

app_name = 'cabinet'
#
#
#
urlpatterns = [
    path('get_events/<int:cabinet_id>/', get_events, name='get_events'),
    # path('calendar/', calendar_view, name='calendar'),
    path('cabinets/<int:cab_id>/', cabinets_view, name='cabinet'),
    path('get_updates/<int:cabinet_id>/', update_calend, name='get_update'),
]

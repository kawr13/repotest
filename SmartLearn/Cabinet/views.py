from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from Cabinet.models import Schedule


# Create your views here.


def get_events(request: HttpRequest) -> JsonResponse:
    events = Schedule.objects.all().values('date_create')
    events = [
        {
            'start': event['date_create'].strftime('%Y-%m-%d %H:%M:%S')
        }
        for event in events
    ]

    return JsonResponse(events, charset='utf-8', safe=False)


def calendar_view(request: HttpRequest) -> render:
    return render(request, 'Cabinet/calend.html')
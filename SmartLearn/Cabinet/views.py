from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from Cabinet.models import Schedule, Cabinet


# Create your views here.


def get_events(request, cabinet_id):
    cabinet = Cabinet.objects.get(id=cabinet_id)
    events = Schedule.objects.filter(cabinets=cabinet).values('date_create')
    print(events)

    events = [
        {
            'start': event['date_create'].strftime('%Y-%m-%d %H:%M:%S')
        }
        for event in events
    ]

    return JsonResponse(events, safe=False)


# def calendar_view(request: HttpRequest) -> render:
#     return render(request, 'Cabinet/calend.html')


def cabinets_view(request: HttpRequest, cab_id: int) -> render:
    context = {
        'title': 'Кабинеты',
        'cabinet_id': cab_id
    }
    return render(request, 'Cabinet/cabinet.html', context=context)
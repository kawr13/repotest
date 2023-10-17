from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from .models import Cabinet, Schedule
from ProfileApp.models import User


# Create your views her
def get_events(request, cabinet_id):
    cabinet = Cabinet.objects.get(id=cabinet_id)
    events = Schedule.objects.filter(cabinet=cabinet).values('date_create', 'date_end', 'title')
    event_data = []
    for event in events:
        print()
        event_data.append({
            'title': event['title'],
            'start': event['date_create'].isoformat(),
            'end': event['date_end'].isoformat() if event['date_end'] else None,
        })
    return JsonResponse(event_data, safe=False)


# def calendar_view(request: HttpRequest) -> render:
#     return render(request, 'CabinetApp/calend.html')


def cabinets_view(request: HttpRequest, cab_id: int) -> render:
    if request.user.id:
        pers = User.objects.get(id=request.user.id).is_authenticated
    else:
        pers = False
    print(pers)
    context = {
        'title': 'Кабинеты',
        'cabinet_id': cab_id,
        'autentic': pers,
    }
    return render(request, 'Cabinet/cabinet.html', context=context)


def update_calend(request: HttpRequest, cabinet_id) -> render:
    if request.method == 'POST':
        date_string = request.POST
        print(date_string)
        if date_string:
            # Получите объект CabinetApp
            cabinet = Cabinet.objects.get(pk=cabinet_id)
            schedule = Schedule.objects.create(
                cabinet=cabinet,
                title=date_string['title'],
                url=date_string['url'],
                date_create=date_string['start'],
                date_end=date_string['end'],
            )
            schedule.save()
            # Создайте новый объект Schedule и свяжите его с CabinetApp

            return redirect('cabinet:cabinet', cab_id=cabinet_id)

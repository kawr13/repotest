from http.client import HTTPResponse

from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from profileapp.forms import UserForm
from profileapp.models import Teacher, User, Category, Tag
# from Cabinet.models import Schedule
from django.contrib import auth
from django.shortcuts import render


def index(request: HttpRequest) -> render:
    context = {
        'users': User.objects.select_related('teacher'),
        'categories': Tag.objects.all(),
    }
    return render(request, 'profileapp/profile/index.html', context=context)


def sort_category(request: HttpRequest, tag_id: int=None) -> render:
    if tag_id:
        context = {
            'users': User.objects.filter(teacher__tags__id=tag_id),
            'categories': Tag.objects.all(),
        }
    else:
        context = {
            'users': User.objects.select_related('teacher'),
            'categories': Tag.objects.all(),
        }

    return render(request, 'profileapp/profile/index.html', context=context)


# def get_events(request: HttpRequest) -> JsonResponse:
#     events = Schedule.objects.all().values('date_create')
#     events = [
#         {
#             'start': event['date_create'].strftime('%Y-%m-%d %H:%M:%S')
#         }
#         for event in events
#     ]
#
#     return JsonResponse(events, safe=False)
#
#
# def calendar_view(request: HttpRequest) -> render:
#     return render(request, 'profileapp/profile/calend.html')


def blog(request: HttpRequest, user_id: int) -> render:
    context = {
        'user': User.objects.select_related('teacher').get(id=user_id),
    }
    return render(request, 'profileapp/profile/blog.html', context=context)


def login(request: HttpRequest) -> render:
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'profileapp/profile/login.html', context=context)
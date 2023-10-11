from http.client import HTTPResponse

from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Learn.forms import UserForm
from Learn.models import Teacher, User, Category, Tag, Schedule
from django.contrib import auth

# Create your views here.


def index(request: HttpRequest) -> render:
    context = {
        'users': User.objects.select_related('teacher'),
        'categories': Tag.objects.all(),
    }
    return render(request, 'Learn/profile/index.html', context=context)


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

    return render(request, 'Learn/profile/index.html', context=context)


def get_events(request: HttpRequest) -> JsonResponse:
    events = Schedule.objects.all().values('date_create')
    events = [
        {
            'start': event['date_create'].strftime('%Y-%m-%d %H:%M:%S')
        }
        for event in events
    ]

    return JsonResponse(events, safe=False)


def calendar_view(request: HttpRequest) -> render:
    return render(request, 'Learn/profile/calend.html')


def blog(request: HttpRequest, user_id: int) -> render:
    context = {
        'user': User.objects.select_related('teacher').get(id=user_id),
    }
    return render(request, 'Learn/profile/blog.html', context=context)


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
    return render(request, 'Learn/profile/login.html', context=context)
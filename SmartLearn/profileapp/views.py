from http.client import HTTPResponse

from django.http import JsonResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from Cabinet.models import Schedule
from profileapp.forms import UserForm, UserRegisterForm
from profileapp.models import Teacher, User, Category, Tag
# from Cabinet.models import Schedule
from django.contrib import auth
from django.shortcuts import render


def index(request: HttpRequest) -> render:
    context = {
        'title': 'Список учителей',
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



def blog(request: HttpRequest, user_id: int) -> render:
    context = {
        'title': 'Блог',
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
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'profileapp/profile/login.html', context=context)


class UserRegisterViews(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'profileapp/profile/register.html'
    success_url = reverse_lazy('profile:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegisterViews, self).get_context_data()
        return context


def profiluser(request: HttpRequest, user_id: int) -> render:
    context = {
        'title': 'Профиль',
        'user': User.objects.select_related('teacher').get(id=user_id),
    }
    return render(request, 'profileapp/profile/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



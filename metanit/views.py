from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import AuthUserForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm  # Замените путь на вашу форму
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Person
from .models import Game
from django.shortcuts import render
import logging
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.conf import settings

logger = logging.getLogger(__name__)

class GameDetailView(DetailView):
    model = Person
    template_name = 'game_detail.html'
    context_object_name = 'game'
    pk_url_kwarg = 'person_id'

def game_detail(request, game_id):
    # Логика для отображения страницы конкретной игры
    return render(request, './game_detail.html', {'game_id': game_id})

def game_list(request):
    games = Game.objects.all()
    return render(request, './game_list.html', {'games': games})

def play_html_view(request, file):
    # Получите путь к HTML-файлу на основе параметра file_id
    html_file_path = os.path.join(settings.BASE_DIR, 'metanit', 'static', 'games', f'{file}.html')

    try:
        # Откройте и прочитайте HTML-файл
        with open(html_file_path, 'r') as html_file:
            html_content = html_file.read()

        # Отправьте содержимое HTML-файла на клиент
        return HttpResponse(html_content)
    except FileNotFoundError:
        # Если файл не найден, верните 404 ошибку
        return HttpResponseNotFound("HTML file not found.")

def play(request):
    # Здесь вы можете добавить логику для списка игр
    return render(request, './game_list.html')

class PersonListView(ListView):
    model = Person
    template_name = 'person_list.html'
    context_object_name = 'persons'

    def get(self, request, *args, **kwargs):
        logger.info('Page "person" requested')

        return super().get(request, *args, **kwargs)


class IndexView(TemplateView):
    template_name = 'index.html'


class PersonDetailView(DetailView):
    model = Person
    template_name = 'detail_person.html'
    context_object_name = 'person'
    pk_url_kwarg = 'person_id'



class MyProjLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('person')

    def get_success_url(self):
        return self.success_url

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('person')
    success_msg = 'User successfully created'

    def form_valid(self, form):
        response = super().form_valid(form)

        # Дополнительный код после успешного создания пользователя
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]  # Используйте 'password1', так как это поле пароля
        aut_user = authenticate(username=username, password=password)

        if aut_user is not None:
            login(self.request, aut_user)

        return response

class MyProjLogout(LogoutView):
    next_page = reverse_lazy('index')


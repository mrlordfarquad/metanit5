from django.contrib import admin
from metanit.views import MyProjLoginView
from metanit.views import MyProjLogout
from django.urls import path
from metanit.views import IndexView
from metanit.views import PersonListView, PersonDetailView
from metanit.views import RegisterView
from metanit.views import GameDetailView, game_list, play_html_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('register_page/', RegisterView.as_view(), name='register_page'),
    path('logout_page/', MyProjLogout.as_view(), name='logout_page'),
    path('login_page/', MyProjLoginView.as_view(), name='login_page'),
    # path('person/<int:person_id>/', PersonDetailView.as_view(), name='person-detail'),
    # path('person/', PersonListView.as_view(), name='person'),
    path('play/', game_list, name='game_list'),
    path('play/<int:game_id>/', GameDetailView.as_view(), name='game_detail'),
    path('play/<str:file>.html/', play_html_view, name='play-html'),
]


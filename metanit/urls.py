from django.urls import path
from metanit.views import PersonDetailView

urlpatterns = [
    path('person/<int:person_id>/', PersonDetailView.as_view(), name='person-detail'),
]

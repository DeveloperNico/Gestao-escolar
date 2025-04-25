from django.urls import path
from .views import *

urlpatterns = [
    path('login/', view=LoginView.as_view(), name='login'),
    path('usuarios/', view=UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', view=UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('professores/', view=ProfessorListCreateView.as_view(), name='professor-list-create'),
    path('professores/<int:pk>/', view=ProfessorRetrieveUpdateDestroyView.as_view(), name='professor-detail'),
    path('disciplinas/', view=DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', view=DisciplinaRetrieveUpdateDestroyView.as_view(), name='disciplina-detail'),
    path('reservas-ambiente/', view=ReservaAmbienteListCreateView.as_view(), name='reserva-ambiente-list-create'),
]
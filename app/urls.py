from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('usuarios/', views.UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', views.UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
    path('professores/', views.ProfessorListCreateView.as_view(), name='professor-list-create'),
    path('professores/<int:pk>/', views.ProfessorRetrieveUpdateDestroyView.as_view(), name='professor-detail'),
    path('disciplinas/', views.DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplinas/<int:pk>/', views.DisciplinaRetrieveUpdateDestroyView.as_view(), name='disciplina-detail'),
    path('reservas-ambiente/', views.ReservaAmbienteListCreateView.as_view(), name='reserva-ambiente-list-create'),
]
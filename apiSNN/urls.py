# existing imports
from django.urls import path
from django.conf.urls import url
from apiSNN import views

urlpatterns = [
    path('libros/', views.ListLibro.as_view()),
    path('libros/<int:pk>/', views.DetailLibro.as_view()),
    path('personas/', views.ListPersona.as_view()),
    path('personas/<int:pk>/', views.DetailPersona.as_view()),
    url(r'^sobrevivencia/$',views.Clasificacion.determinarSobrevivencia),
    url(r'^predecir/',views.Clasificacion.predecir),
    url(r'^$',views.Autenticacion.singIn),
    url(r'^postsign/',views.Autenticacion.postsign),
]
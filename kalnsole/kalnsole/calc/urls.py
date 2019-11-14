from django.urls import path

from kalnsole.kalnsole.calc import views
urlpatterns = [
    path('', views.home, name='home')
]
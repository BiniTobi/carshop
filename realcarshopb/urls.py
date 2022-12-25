from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail_page, name='detail'),
    path('cars', views.cars_page, name='cars'),

]
from django.urls import path
from . import views

app_name = 'binicarproject'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail_page, name='detail'),

]
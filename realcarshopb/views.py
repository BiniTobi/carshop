from django.shortcuts import render,get_object_or_404
from .models import Homecars


def index(request):
  
  homecars = Homecars.objects.all()
  return render(request, "index.html", {'homecars':homecars})

def detail_page(request,id):
   obj = get_object_or_404(Homecars,pk=id)
   return render(request,'detail.html',{'obj':obj})


def cars_page(request):
  cars = Homecars.objects.all()
  return render(request, "cars.html", {'cars':cars})


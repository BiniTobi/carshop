from django.shortcuts import render,get_object_or_404
from .models import Homepage
from django.core.paginator import Paginator
def index(request):
  
  homepage = Homepage.objects.all()
  p = Paginator(Homepage.objects.all(),9)
  
  page = request.GET.get('page')
  homepages = p.get_page(page)
  nums = "a" * homepages.paginator.num_pages

  return render(request, "index.html", {'homepage':homepage,
  'homepages':homepages,
  'nums':nums
  })

def detail_page(request,id):
   obj = get_object_or_404(Homepage,pk=id)
   return render(request,'car-details.html',{'obj':obj})


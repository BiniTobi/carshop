from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from django.views.static import serve
# from django.conf.urls import url


urlpatterns = [
    path('', include('binicarproject.urls')),
    path('admin/', admin.site.urls),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

admin.site.site_header = "Mekina Adminstration Page"
admin.site.site_title = "Mekina Admin Page"
admin.site.index_title = "Welcome Mekina Admin user"

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
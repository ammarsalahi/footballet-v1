from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from siteapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('tag/<str:name>',get_news,name='tag'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
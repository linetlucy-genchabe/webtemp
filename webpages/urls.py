from django.urls import re_path as url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'register/$',views.register, name='register' ),
    url(r'accounts/login/$',views.user_login, name='login'),
    url(r'logout/$',views.signout),
    
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
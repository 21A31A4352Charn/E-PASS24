from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',login,name='login'),
    path('notf',notifications,name='notifictions'),
    path('signup',home,name='signup'),
    path('user',user,name='user'),
    path('reports',reports,name='reports'),
    path('logout',logout,name='logout'),
    path('inbox',inbox,name='inbox'),
    path('open',open,name='open'),
    path('accept',accept,name='accept'),
    path('dec',decline,name='decline'),
    path('ads',ads,name='ads'),
    path('anew',anew,name='anew'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



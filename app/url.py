from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('login',views.login,name='login'),
path('doc',views.doc,name='doc'),
path('pdf',views.pdf,name='pdf'),
path('excel',views.excel,name='excel'),
path('logout',views.logout,name='logout'),
path('register',views.register,name='register'),
]
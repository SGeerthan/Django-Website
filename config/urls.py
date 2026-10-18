
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('students/', views.students_page, name='students'),
]

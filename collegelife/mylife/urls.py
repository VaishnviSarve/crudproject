from django.contrib import admin
from django.urls import path
from mylife import views

urlpatterns = [
    path('',views.life,name='life'),
    path('index',views.index,name='index'),
    path('update/<int:rollno>',views.update,name='update'),
    path('update/updaterequest/<int:rollno>',views.updaterequest,name='updaterequest'),
    path('delete/<int:rollno>',views.delete,name='delete'),
    
]

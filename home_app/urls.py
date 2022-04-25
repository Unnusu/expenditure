from django.urls import path
from home_app import views


urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('add/',views.add, name='add'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('delete_all/',views.delete_all,name="del_all")  
]
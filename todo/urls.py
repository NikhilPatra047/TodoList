from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
    #This is how dynamic urls are created.
]

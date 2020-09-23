from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('todo', views.todo, name='todo'),
    path('delete/<int:id>', views.delete),

]
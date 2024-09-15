from django.urls import path
from . import views

urlpatterns = [
    path('', views.bus_list, name='bus_list'),
    path('bus/<int:pk>/', views.bus_detail, name='bus_detail'),
    path('add_bus/', views.add_bus, name='add_bus'),
    path('bus/<int:pk>/add_student/', views.add_student, name='add_student'),
    path('bus/<int:pk>/update/', views.update_bus, name='update_bus'),
    path('bus/<int:pk>/delete/', views.delete_bus, name='delete_bus'),
    path('bus/<int:bus_id>/remove_student/<int:student_id>/', views.remove_student, name='remove_student'),
]

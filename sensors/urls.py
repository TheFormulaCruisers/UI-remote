from django.urls import path
from sensors import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sensor_id>', views.sensor)
]

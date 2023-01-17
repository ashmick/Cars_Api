from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_list),
    path('<pk>/ ', views.cars_list),
]

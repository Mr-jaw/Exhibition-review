from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addrecord/', views.addrecord, name='add'),
    path('addrecord/thankyou', views.thankyou, name='thankyou')
]
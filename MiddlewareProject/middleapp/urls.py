from django.urls import path
from middleapp.views import *

urlpatterns = [
    path('home/', home),
    path('home1/', home_view),
    path('home2/', home2),
    path('home3/', home3),
    path('home4/', home4),
]

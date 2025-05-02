from django.urls import path
from .views import CarAPIView


urlpatterns = [
    path('car/', CarAPIView.as_view())

]
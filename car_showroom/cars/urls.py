from django.urls import path
from .views import CarAPIView, CarDetailAPIView


urlpatterns = [
    path('car/', CarAPIView.as_view()),
    path('car/<int:id>/', CarDetailAPIView.as_view())

]
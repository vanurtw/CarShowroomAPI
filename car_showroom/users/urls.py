from django.urls import path
from .views import RegistrationAPIView, UserAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('user/', UserAPIView.as_view()),

]

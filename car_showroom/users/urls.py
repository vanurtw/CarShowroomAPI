from django.urls import path
from .views import RegistrationAPIView, UserAPIView, ProfileAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('user/me/', UserAPIView.as_view()),
    path('profile/', ProfileAPIView.as_view()),

]

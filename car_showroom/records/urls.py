from django.urls import path
from .views import RecordAPIView, RecordDetailAPIView, ServiceAPIView

urlpatterns = [
    path('record/', RecordAPIView.as_view()),
    path('record/<int:id>/', RecordDetailAPIView.as_view()),
    path('services/', ServiceAPIView.as_view())
]

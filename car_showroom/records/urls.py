from django.urls import path
from .views import RecordAPIView, RecordDetailAPIView

urlpatterns = [
    path('record', RecordAPIView.as_view()),
    path('record/<int:id>/', RecordDetailAPIView.as_view()),

]

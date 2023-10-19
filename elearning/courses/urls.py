from django.urls import path
from .views import LessonListAPIView

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
]

from django.urls import path
from .views import LessonListAPIView, LessonDetailAPIView, ProductStatAPIView

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('product-stats/', ProductStatAPIView.as_view(), name='product-stats'),
]

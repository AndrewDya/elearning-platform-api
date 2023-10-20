from django.urls import path
from .views import ProductStatAPIView, LessonsByUsersAPIView

urlpatterns = [
    path('lessons/by-user/', LessonsByUsersAPIView.as_view(), name='lessons-by-user'),
    path('product-stats/', ProductStatAPIView.as_view(), name='product-stats'),
]

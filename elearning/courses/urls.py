from django.urls import path
from .views import ProductStatAPIView, LessonsByUsersAPIView, \
    LessonsByProductAPIView

urlpatterns = [
    path('lessons/by-user/', LessonsByUsersAPIView.as_view(), name='lessons-by-user'),
    path('lessons/by-product/', LessonsByProductAPIView.as_view(), name='lessons-by-product'),
    path('product-stats/', ProductStatAPIView.as_view(), name='product-stats'),
]

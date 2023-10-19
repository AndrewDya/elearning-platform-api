from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Lesson, UserProductAccess
from .serializers import LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.all()
        else:
            product_ids = UserProductAccess.objects.filter(user=user).values_list('product_id', flat=True)
            return Lesson.objects.filter(products__in=product_ids)

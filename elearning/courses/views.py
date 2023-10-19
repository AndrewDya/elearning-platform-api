from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Lesson, UserProductAccess, Product, LessonView, User
from .serializers import LessonSerializer, LessonDetailSerializer
from django.db.models import Sum


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Lesson.objects.all()
        else:
            product_ids = UserProductAccess.objects.filter(user=user).values_list('product_id', flat=True)
            return Lesson.objects.filter(products__in=product_ids)


class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonDetailSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        if user.is_anonymous:
            return Lesson.objects.filter(products__id=product_id)
        else:
            product_ids = UserProductAccess.objects.filter(user=user).values_list('product_id', flat=True)
            if product_id in product_ids:
                return Lesson.objects.filter(products__id=product_id)
            else:
                return Lesson.objects.none()


class ProductStatAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        product_stats = []

        for product in products:
            total_lessons_watched = LessonView.objects.filter(lesson__products=product).count()
            total_time_watched = LessonView.objects.filter(lesson__products=product).aggregate(
                Sum('viewed_time_seconds'))['viewed_time_seconds__sum']
            total_students = UserProductAccess.objects.filter(product=product).count()
            acquisition_percentage = (total_students /
                                      User.objects.count()) * 100 if User.objects.count() > 0 else 0

            product_stat = {
                'product_id': product.id,
                'product_name': product.name,
                'lessons_watched': total_lessons_watched,
                'total_time_watched': total_time_watched or 0,
                'total_students': total_students,
                'acquisition_percentage': acquisition_percentage,
            }

            product_stats.append(product_stat)

        return Response(product_stats, status=status.HTTP_200_OK)

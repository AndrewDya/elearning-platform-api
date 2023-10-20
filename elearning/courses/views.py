from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Lesson, UserProductAccess, Product, LessonView, User
from .serializers import ProductStatSerializer, UserLessonSerializer
from django.db.models import Sum


class LessonsByUsersAPIView(generics.ListAPIView):
    serializer_class = UserLessonSerializer

    def get_queryset(self):
        users = User.objects.all()
        user_lessons = []

        for user in users:
            lessons = []

            for product_access in UserProductAccess.objects.filter(user=user):
                product = product_access.product
                product_lessons = Lesson.objects.filter(products=product)

                for lesson in product_lessons:
                    lesson_view = LessonView.objects.filter(user=user,
                                                            lesson=lesson).last()
                    status = "Просмотрено" if (lesson_view and (lesson_view.viewed_time_seconds >= lesson.duration_seconds * 0.8)) else "Не просмотрено"
                    viewed_time = lesson_view.viewed_time_seconds if lesson_view else 0

                    lesson_data = {
                        'lesson_id': lesson.id,
                        'lesson_name': lesson.name,
                        'video_link': lesson.video_link,
                        'duration_seconds': lesson.duration_seconds,
                        'product_name': product.name,
                        'status': status,
                        'viewed_time_seconds': viewed_time,
                    }
                    lessons.append(lesson_data)

            user_lesson_data = {
                'user_name': user.name,
                'lessons': lessons
            }
            user_lessons.append(user_lesson_data)

        return user_lessons


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
            acquisition_percentage = round((total_students /
                                          User.objects.count()) * 100, 0) if User.objects.count() > 0 else 0

            product_stat = ProductStatSerializer(data={
                'product_id': product.id,
                'product_name': product.name,
                'lessons_watched': total_lessons_watched,
                'total_time_watched': total_time_watched or 0,
                'total_students': total_students,
                'acquisition_percentage': acquisition_percentage,
            })

            if product_stat.is_valid():
                product_stats.append(product_stat.data)

        return Response(product_stats, status=status.HTTP_200_OK)

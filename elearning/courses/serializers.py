from rest_framework import serializers
from .models import Lesson


class LessonDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    last_viewed = serializers.DateTimeField(source='get_last_viewed')

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link', 'duration_seconds']


class ProductStatSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    lessons_watched = serializers.IntegerField()
    total_time_watched = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.DecimalField(max_digits=5,
                                                      decimal_places=2)

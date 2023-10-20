from rest_framework import serializers


class UserLessonSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    lessons = serializers.ListField(child=serializers.DictField())


class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    lessons = serializers.ListField(child=serializers.DictField())


class ProductStatSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    lessons_watched = serializers.IntegerField()
    total_time_watched = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.IntegerField()

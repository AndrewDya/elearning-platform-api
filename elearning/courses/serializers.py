from rest_framework import serializers


class UserLessonSerializer(serializers.Serializer):
    """
    Сериализатор для пользовательских уроков.

    Поля:
    - user_name (str): Имя пользователя.
    - lessons (list of dict): Список уроков, каждый урок представлен
    в виде словаря с информацией о уроке.
    """

    user_name = serializers.CharField()
    lessons = serializers.ListField(child=serializers.DictField())


class ProductSerializer(serializers.Serializer):
    """
    Сериализатор для продукта.

    Поля:
    - product_name (str): Название продукта.
    - lessons (list of dict): Список уроков, каждый урок представлен
    в виде словаря с информацией о уроке.
    """

    product_name = serializers.CharField()
    lessons = serializers.ListField(child=serializers.DictField())


class ProductStatSerializer(serializers.Serializer):
    """
    Сериализатор для статистики продукта.

    Поля:
    - product_id (int): Идентификатор продукта.
    - product_name (str): Название продукта.
    - lessons_watched (int): Количество просмотренных уроков.
    - total_time_watched (int): Общее время просмотра уроков.
    - total_students (int): Общее количество студентов.
    - acquisition_percentage (int): Процент приобретения продукта.
    """

    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    lessons_watched = serializers.IntegerField()
    total_time_watched = serializers.IntegerField()
    total_students = serializers.IntegerField()
    acquisition_percentage = serializers.IntegerField()

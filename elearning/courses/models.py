from django.db import models


class User(models.Model):
    """
    Модель, представляющая пользователя в системе.

    Поля:
    - `name`: Имя пользователя (строка, максимум 100 символов).
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Owner(models.Model):
    """
    Модель, представляющая владельца продукта.

    Поля:
    - `name`: Имя владельца (строка, максимум 100 символов).
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель, представляющая продукт.

    Поля:
    - `name`: Название продукта (строка, максимум 100 символов).
    - `owner`: Внешний ключ, связывающий продукт с владельцем.
    """

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Модель, представляющая урок.

    Поля:
    - `name`: Название урока (строка, максимум 100 символов).
    - `video_link`: Ссылка на видео-урок.
    - `duration_seconds`: Продолжительность урока в секундах.
    - `products`: Многие ко многим отношение к продуктам.
    """

    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name


class UserProductAccess(models.Model):
    """
    Модель, представляющая доступ пользователя к продукту.

    Поля:
    - `access_type`: Тип доступа (постоянный или временный).
    - `access_granted`: Флаг, указывающий, предоставлен ли доступ.
    - `user`: Внешний ключ, связывающий пользователя с продуктом.
    - `product`: Внешний ключ, связывающий продукт с пользователем.
    """

    ACCESS_TYPE_CHOICES = [
        (1, "Постоянный доступ"),
        (2, "Временный доступ"),
    ]

    access_type = models.IntegerField(choices=ACCESS_TYPE_CHOICES, default=1)
    access_granted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class LessonView(models.Model):
    """
    Модель, представляющая просмотр урока пользователем.

    Поля:
    - `user`: Внешний ключ, связывающий пользователя с уроком.
    - `lesson`: Внешний ключ, связывающий урок с пользователем.
    - `viewed_time_seconds`: Время просмотра урока в секундах.
    - `status`: Статус просмотра (просмотрено или не просмотрено).
    - `percent_completed`: Процент завершения урока.
    """

    STATUS_CHOICES = [
        (1, "Просмотрено"),
        (2, "Не просмотрено"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time_seconds = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    percent_completed = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.lesson and self.lesson.duration_seconds > 0:
            if self.viewed_time_seconds > self.lesson.duration_seconds:
                self.viewed_time_seconds = self.lesson.duration_seconds
            self.percent_completed = (self.viewed_time_seconds
                                      / self.lesson.duration_seconds) * 100
        else:
            self.percent_completed = 0
        super(LessonView, self).save(*args, **kwargs)

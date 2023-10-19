from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class LessonView(models.Model):
    STATUS_CHOICES = [
        (1, "Просмотрено"),
        (2, "Не просмотрено"),
    ]

    user = models.ManyToManyField(User)
    lesson = models.ManyToManyField(Lesson)
    viewed_time_seconds = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

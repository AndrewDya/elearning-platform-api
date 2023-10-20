from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Owner(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    video_link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


class UserProductAccess(models.Model):
    ACCESS_TYPE_CHOICES = [
        (1, "Постоянный доступ"),
        (2, "Временный доступ"),
    ]

    access_type = models.IntegerField(choices=ACCESS_TYPE_CHOICES, default=1)
    access_granted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class LessonView(models.Model):
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

from django.test import TestCase
from django.urls import reverse
from .models import User, Owner, Product, Lesson, UserProductAccess, LessonView


class LessonsByProductAPITestCase(TestCase):

    def setUp(self):
        owner1 = Owner.objects.create(name="Owner1")
        product1 = Product.objects.create(name="Product1", owner=owner1)
        lesson1 = Lesson.objects.create(name="Lesson1", video_link="video1",
                                        duration_seconds=300)
        lesson1.products.set([product1])

    def test_lessons_by_product_api(self):
        url = reverse('lessons-by-product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class LessonsByUsersAPITestCase(TestCase):

    def setUp(self):
        user1 = User.objects.create(name="User1")
        user2 = User.objects.create(name="User2")
        owner1 = Owner.objects.create(name="Owner1")
        product1 = Product.objects.create(name="Product1", owner=owner1)
        lesson1 = Lesson.objects.create(name="Lesson1", video_link="video1",
                                        duration_seconds=300)
        lesson2 = Lesson.objects.create(name="Lesson2", video_link="video2",
                                        duration_seconds=400)
        lesson1.products.set([product1])
        lesson2.products.set([product1])
        UserProductAccess.objects.create(user=user1, product=product1,
                                         access_type=1, access_granted=True)
        UserProductAccess.objects.create(user=user2, product=product1,
                                         access_type=1, access_granted=True)
        LessonView.objects.create(user=user1, lesson=lesson1,
                                  viewed_time_seconds=250, status="Просмотрено")
        LessonView.objects.create(user=user1, lesson=lesson2,
                                  viewed_time_seconds=350, status="Просмотрено")

    def test_lessons_by_users_api(self):
        url = reverse('lessons-by-user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        user1_data = next(item for item in response.data if item["user_name"] == "User1")
        self.assertEqual(len(user1_data['lessons']), 2)
        self.assertEqual(user1_data['lessons'][0]['status'], "Просмотрено")
        self.assertEqual(user1_data['lessons'][1]['status'], "Просмотрено")
        self.assertEqual(user1_data['lessons'][0]['viewed_time_seconds'], 250)
        self.assertEqual(user1_data['lessons'][1]['viewed_time_seconds'], 350)

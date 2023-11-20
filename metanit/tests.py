# from django.test import TestCase
#
# class TestIndex(TestCase):
#     def test_index(self):
#         response = self.client.get('//')
#         self.assertEqual(response.status_code, 200)
#
#     def test_text(self):
#         response = self.client.get('//')
#         self.assertIn('', response.content.decode())

from django.urls import reverse
from .models import Person
from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class PersonListViewTest(TestCase):
    def setUp(self):
        Person.objects.create(name='John', age='21')

    def test_person_list_view(self):
        url = reverse('person')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'person_list.html')

class MyProjLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_success(self):
        response = self.client.post(reverse_lazy('login_page'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse_lazy('person'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_failure(self):
        response = self.client.post(reverse_lazy('login_page'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class RegisterViewTest(TestCase):
    def test_register_view_success(self):
        response = self.client.post(reverse_lazy('register_page'), {'username': 'testuser1', 'password': 'testpassword'})
        self.assertRedirects(response, reverse_lazy('person'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_register_view_failure(self):
        response = self.client.post(reverse_lazy('register_page'), {'username': 'testuser', 'password1': 'testpassword', 'password2': 'wrongpassword'})
        self.assertTemplateUsed(response, 'register.html')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

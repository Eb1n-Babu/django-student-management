from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Student

class StudentHTMLTests(TestCase):
    def setUp(self): self.student = Student.objects.create(name="Asha Rao", email="asha@example.com", age=20, course="Computing")
    def test_fbv_list_renders_students(self):
        response = self.client.get(reverse("student-list")); self.assertEqual(response.status_code, 200); self.assertContains(response, "Asha Rao")
    def test_cbv_list_renders_students(self):
        response = self.client.get(reverse("student-list-cbv")); self.assertEqual(response.status_code, 200); self.assertContains(response, "Asha Rao")
    def test_fbv_create_and_delete(self):
        response = self.client.post(reverse("student-create"), {"name":"Ben Lee","email":"ben@example.com","age":19,"course":"Math"}); self.assertRedirects(response, reverse("student-list")); self.assertTrue(Student.objects.filter(email="ben@example.com").exists())
        response = self.client.post(reverse("student-delete", args=[self.student.pk])); self.assertRedirects(response, reverse("student-list")); self.assertFalse(Student.objects.filter(pk=self.student.pk).exists())
    def test_cbv_create_and_update(self):
        response = self.client.post(reverse("student-create-cbv"), {"name":"Ben Lee","email":"ben@example.com","age":19,"course":"Math"}); self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse("student-update-cbv", args=[self.student.pk]), {"name":"Asha Rao","email":"asha@example.com","age":21,"course":"Physics"}); self.assertEqual(response.status_code, 302); self.student.refresh_from_db(); self.assertEqual(self.student.course, "Physics")

class StudentAPITests(TestCase):
    def setUp(self):
        self.client = APIClient(); self.student = Student.objects.create(name="Asha Rao", email="asha@example.com", age=20, course="Computing")
        self.data = {"name":"Ben Lee","email":"ben@example.com","age":19,"course":"Math"}
    def test_fbv_api_list_create_update_delete(self):
        url = reverse("api-student-list"); self.assertEqual(self.client.get(url).status_code, 200)
        created = self.client.post(url, self.data, format="json"); self.assertEqual(created.status_code, 201); pk = created.data["id"]; detail = reverse("api-student-detail", args=[pk])
        self.assertEqual(self.client.patch(detail, {"age":20}, format="json").status_code, 200); self.assertEqual(self.client.delete(detail).status_code, 204)
    def test_fbv_api_validates_and_gets_detail(self):
        self.assertEqual(self.client.get(reverse("api-student-detail", args=[self.student.pk])).data["name"], "Asha Rao")
        self.assertEqual(self.client.post(reverse("api-student-list"), {"email":"bad"}, format="json").status_code, 400)
    def test_model_viewset_crud(self):
        collection = "/api/viewset/students/"; created = self.client.post(collection, self.data, format="json"); self.assertEqual(created.status_code, 201); detail = f"{collection}{created.data['id']}/"
        self.assertEqual(self.client.get(collection).status_code, 200); self.assertEqual(self.client.put(detail, {**self.data,"name":"Benny Lee"}, format="json").status_code, 200)
        self.assertEqual(self.client.delete(detail).status_code, 204)

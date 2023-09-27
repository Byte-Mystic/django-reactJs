from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MyAPITestCase(APITestCase):
    def test_list_objects(self):
        response = self.client.get(reverse("notes"))
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # def test_create_object(self):
    #     url = reverse("create-note")
    #     data = {"body": "Testing"}
    #     response = self.client.post(url, data, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data["body"], "Testing")

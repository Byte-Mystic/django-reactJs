from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Notes
from api.serializers import NoteSerializer


class MyAPITestCase(APITestCase):
    def setUp(self):
        self.note = Notes.objects.create(body="Initial Note Content")

    def test_list_notes(self):
        response = self.client.get(reverse("notes"))
        print("HELLO WORLD")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_note(self):
        url = reverse("create-note")
        data = {"body": "Testing"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["body"], "Testing")

    def test_update_note(self):
        updated_data = {"body": "Updated Note Content"}
        url = reverse("update-note", args=[self.note.id])
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()
        self.assertEqual(self.note.body, "Updated Note Content")

        # Check if the response data matches the updated data
        self.assertEqual(response.data, NoteSerializer(self.note).data)

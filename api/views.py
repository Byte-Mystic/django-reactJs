from rest_framework.response import Response
from rest_framework.views import APIView
import datetime
from mynotes import db
from rest_framework.parsers import JSONParser
from rest_framework import status
from bson import ObjectId, json_util


class NotesListView(APIView):
    NOTES = db["Notes"]

    def get(self, request):
        notes = list(self.NOTES.find({}).sort("updated", -1))
        serialized_notes = [json_util.dumps(note) for note in notes]
        return Response(serialized_notes)

    def post(self, request):
        json_parser = JSONParser()
        note_data = json_parser.parse(request)
        note_data["created"] = datetime.datetime.now(tz=datetime.timezone.utc)
        note_data["updated"] = datetime.datetime.now(tz=datetime.timezone.utc)
        inserted_note = self.NOTES.insert_one(note_data)
        response_data = {
            "message": "Note created successfully",
            "note_id": str(inserted_note.inserted_id),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class NoteDetailView(APIView):
    NOTES = db["Notes"]

    def get(self, request, pk):
        if request.method == "GET":
            note = self.NOTES.find_one({"_id": ObjectId(pk)})
            if note:
                serialized_note = json_util.dumps(note)
                return Response(serialized_note, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND
                )

    def put(self, request, pk):
        json_parser = JSONParser()
        update_data = json_parser.parse(request)
        if "_id" in update_data:
            del update_data["_id"]
        update_data["updated"] = datetime.datetime.now(tz=datetime.timezone.utc)
        result = self.NOTES.update_one({"_id": ObjectId(pk)}, {"$set": update_data})
        if result.modified_count > 0:
            return Response(
                {"detail": "Updated Successfully"}, status=status.HTTP_200_OK
            )
        return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        note = self.NOTES.delete_one({"_id": ObjectId(pk)})
        if note:
            return Response(
                {"detail": "Deleted Successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND
            )


class RoutesView(APIView):
    def get(self, request):
        routes = [
            {
                "Endpoint": "/notes/",
                "method": "GET",
                "body": None,
                "description": "Returns an Array of notes",
            },
            {
                "Endpoint": "/notes/id",
                "method": "GET",
                "body": None,
                "description": "Returns a single note object",
            },
            {
                "Endpoint": "/notes/create/",
                "method": "POST",
                "body": None,
                "description": "Creates new note with data sent in post request.",
            },
            {
                "Endpoint": "/notes/id/update/",
                "method": "PUT",
                "body": {"body": ""},
                "description": "Updates an existing note with data sent in post request",
            },
            {
                "Endpoint": "/notes/id/delete/",
                "method": "DELETE",
                "body": None,
                "description": "Deletes an existing note.",
            },
        ]
        return Response(routes)

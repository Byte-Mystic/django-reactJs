from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
from mynotes import db
from rest_framework.parsers import JSONParser
from rest_framework import status
from bson import ObjectId, json_util

NOTES = db["Notes"]


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        notes = list(NOTES.find({}).sort("updated", -1))
        serialized_notes = [json_util.dumps(note) for note in notes]
        return Response(serialized_notes)

    if request.method == "POST":
        json_parser = JSONParser()
        note_data = json_parser.parse(request)
        note_data["created"] = datetime.datetime.now(tz=datetime.timezone.utc)
        note_data["updated"] = datetime.datetime.now(tz=datetime.timezone.utc)
        inserted_note = NOTES.insert_one(note_data)
        response_data = {
            "message": "Note created successfully",
            "note_id": str(inserted_note.inserted_id),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        note = NOTES.find_one({"_id": ObjectId(pk)})
        if note:
            serialized_note = json_util.dumps(note)
            return Response(serialized_note, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND
            )

    if request.method == "PUT":
        json_parser = JSONParser()
        update_data = json_parser.parse(request)
        if "_id" in update_data:
            del update_data["_id"]
        update_data["updated"] = datetime.datetime.now(tz=datetime.timezone.utc)
        result = NOTES.update_one({"_id": ObjectId(pk)}, {"$set": update_data})
        if result.modified_count > 0:
            return Response(
                {"detail": "Updated Successfully"}, status=status.HTTP_200_OK
            )
        return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        note = NOTES.delete_one({"_id": ObjectId(pk)})
        if note:
            return Response(
                {"detail": "Deleted Successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND
            )


@api_view(["GET"])
def getRoutes(request):
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

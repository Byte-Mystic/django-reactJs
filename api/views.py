from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer
from .utils import getNoteslist, createNote, listNote, updateNote, deleteNote


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


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        return getNoteslist()
    if request.method == "POST":
        return createNote(request)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        return listNote(request, pk)

    if request.method == "PUT":
        return updateNote(request, pk)

    if request.method == "DELETE":
        return deleteNote(request, pk)

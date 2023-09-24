from rest_framework.response import Response
from .models import Notes
from .serializers import NoteSerializer


def getNoteslist():
    notes = Notes.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def createNote(request):
    data = request.data
    note = Notes.objects.create(body=data["body"])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def listNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


def updateNote(request, pk):
    data = request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def deleteNote(request, pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")

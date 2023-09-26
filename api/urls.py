from django.urls import path
from . import views

urlpatterns = [
    path("", views.RoutesView.as_view(), name="routes"),
    path("notes/", views.NotesListView.as_view(), name="notes"),
    path("notes/<str:pk>/", views.NoteDetailView.as_view(), name="notes"),
]

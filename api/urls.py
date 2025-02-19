from django.urls import path
from . import views


urlpatterns = [
    path("notes/", views.NoteListCreateView.as_view(), name="notes"),
    path("notes/<int:pk>/", views.NoteDeleteView.as_view(), name="delete_note"),
]

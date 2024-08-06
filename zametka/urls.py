from django.urls import path
from zametka import views

app_name = "zametka"

urlpatterns = [
    path("", views.NoteListView.as_view(), name="note-list"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note-details"),
    path("note-form", views.NoteCreateView.as_view(), name="note-create"),
]

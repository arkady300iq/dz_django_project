from django.shortcuts import render
from django.urls import reverse_lazy
from zametka.models import Note
from django.views.generic import ListView, DetailView, CreateView
from zametka.forms import NoteForm

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "note/note_list.html"

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "note/note_details.html"

class NoteCreateView(CreateView):
    model = Note
    template_name = "note/note_form.html"
    form_class = NoteForm
    success_url = reverse_lazy("zametka:note-list")



    







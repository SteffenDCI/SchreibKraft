from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView

# Create your views here.

from .models import Notes

# class-based view


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"


def list(request):
    all_notes = Notes.objects.all()

    return render(request, 'notes/notes_list.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)

    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(request, 'notes/notes_detail.html', {'note': note})

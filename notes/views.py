from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Note


@login_required
def notes_view(request):
    notes = Note.objects.filter(owner=request.user).order_by("-id").all()
    return render(request, "notes/list.html", {
        "notes": list(map(lambda note: note.get_text(), notes)),
    })


@login_required
def new_note_view(request):
    if request.method != "POST":
        return redirect("notes")
    text = request.POST["note"]
    note = Note(owner=request.user)
    note.set_text(text)
    note.save()
    return redirect("notes")

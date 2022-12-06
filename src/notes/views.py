from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Note


@login_required
def notes_view(request):
    notes = Note.objects.order_by("-id").all()
    rsa_e = request.user.profile.rsa_e
    return render(request, "notes/list.html", {
        "rsa_e": rsa_e,
        "notes": list(map(lambda note: note.encrypt(rsa_e), notes)),
    })


@login_required
def new_note_view(request):
    if request.method != "POST":
        return redirect("notes")
    text = request.POST["note"]
    Note(text=text).save()
    return redirect("notes")

from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('notes/', views.notes_view, name='notes'),
    path('new/', views.new_note_view, name='new'),
    path('', lambda req: redirect("notes")),
]

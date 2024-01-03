from django.shortcuts import render

# Create your views here.

myNotes = [
    {"id":1, "title":"first Note", "entries":["entry 1.1", "entry 1.3", "entry 1.3"]},
    {"id":2, "title":"second Note", "entries":["entry 2.1", "entry 2.2", "entry 2.3"]},
    {"id":3, "title":"third Note", "entries":["entry 3.1", "entry 3.2", "entry 3.3"]}
]

def index(request):
    return render(request, "notes/index.html")

def notes(request):
    notes = myNotes
    context = {"notes":notes}

    return render(request, "notes/notes.html", context)

def note(request, note_id):
    note = {}
    for myNote in myNotes:
        if myNote["id"] == note_id:
            note = myNote
        
    entries = note["entries"]
    context = {"note":note, "entries":entries}

    return render(request, "notes/note.html", context)
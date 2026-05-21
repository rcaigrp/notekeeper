import json
import os

STORAGE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")

def _load_notes():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, 'r') as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []

def _save_notes(notes):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(notes, f)

def add_note(text):
    notes = _load_notes()
    new_note = {"id": len(notes) + 1, "text": text}
    notes.append(new_note)
    _save_notes(notes)
    return new_note

def get_notes():
    return _load_notes()

def delete_note(note_id):
    notes = _load_notes()
    notes = [n for n in notes if n["id"] != note_id]
    _save_notes(notes)

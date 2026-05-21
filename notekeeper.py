import json
import os

DEFAULT_STORAGE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")

def _get_storage_file(storage_file=None):
    return storage_file or DEFAULT_STORAGE_FILE

def _load_notes(storage_file=None):
    storage_file = _get_storage_file(storage_file)
    if not os.path.exists(storage_file):
        return []
    with open(storage_file, 'r') as f:
        return json.load(f)

def _save_notes(notes, storage_file=None):
    storage_file = _get_storage_file(storage_file)
    with open(storage_file, 'w') as f:
        json.dump(notes, f)

def add_note(note, storage_file=None):
    notes = _load_notes(storage_file)
    note_id = str(len(notes) + 1)
    note_entry = {"id": note_id, "content": note}
    notes.append(note_entry)
    _save_notes(notes, storage_file)
    return note_id

def get_notes(storage_file=None):
    return _load_notes(storage_file)

def delete_note(note_id, storage_file=None):
    notes = _load_notes(storage_file)
    notes = [n for n in notes if n["id"] != note_id]
    _save_notes(notes, storage_file)

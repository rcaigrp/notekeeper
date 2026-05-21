import json
import os

STORAGE_PATH = None

def set_storage_path(path):
    global STORAGE_PATH
    STORAGE_PATH = path

def load_notes():
    if STORAGE_PATH is None:
        STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
    if not os.path.exists(STORAGE_PATH):
        return []
    with open(STORAGE_PATH, 'r') as f:
        return json.load(f)

def save_notes(notes):
    if STORAGE_PATH is None:
        STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
    with open(STORAGE_PATH, 'w') as f:
        json.dump(notes, f)

def add_note(title, content):
    notes = load_notes()
    new_note = {"id": str(len(notes) + 1), "title": title, "content": content}
    notes.append(new_note)
    save_notes(notes)
    return new_note

def get_notes():
    return load_notes()

def delete_note(note_id):
    notes = load_notes()
    filtered = [n for n in notes if n["id"] != str(note_id)]
    if len(filtered) < len(notes):
        save_notes(filtered)
        return True
    return False

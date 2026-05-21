import json
import os

STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")

def _load():
    if not os.path.exists(STORAGE_PATH):
        return []
    with open(STORAGE_PATH, "r") as f:
        try:
            return json.load(f)
        except Exception:
            return []

def _save(data):
    with open(STORAGE_PATH, "w") as f:
        json.dump(data, f)

def add_note(note_id, content):
    data = _load()
    for item in data:
        if item["id"] == note_id:
            return False
    data.append({"id": note_id, "content": content})
    _save(data)
    return True

def get_notes():
    return _load()

def delete_note(note_id):
    data = _load()
    new_data = [n for n in data if n["id"] != note_id]
    if len(new_data) < len(data):
        _save(new_data)
        return True
    return False

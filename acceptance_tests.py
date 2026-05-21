import pytest
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_criterion_1_import():
    try:
        import notekeeper
        assert True
    except ImportError:
        assert False

def test_criterion_2_add_note():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
    if os.path.exists(file_path):
        os.remove(file_path)
    
    from notekeeper import add_note
    note_id = add_note("Test Title", "Test Content")
    assert note_id == "1"
    assert os.path.exists(file_path)
    with open(file_path, "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["title"] == "Test Title"
    assert data[0]["content"] == "Test Content"

def test_criterion_3_get_notes():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
    if os.path.exists(file_path):
        os.remove(file_path)
    
    from notekeeper import add_note, get_notes
    add_note("Note 1", "Content 1")
    add_note("Note 2", "Content 2")
    notes = get_notes()
    assert len(notes) == 2
    assert notes[0]["title"] == "Note 1"
    assert notes[1]["title"] == "Note 2"

def test_criterion_4_delete_note():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")
    if os.path.exists(file_path):
        os.remove(file_path)
    
    from notekeeper import add_note, delete_note, get_notes
    add_note("Note 1", "Content 1")
    add_note("Note 2", "Content 2")
    delete_note("2")
    notes = get_notes()
    assert len(notes) == 1
    assert notes[0]["title"] == "Note 1"

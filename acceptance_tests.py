import os
import sys
import pytest
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import notekeeper

@pytest.fixture
def temp_storage():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as tmp:
        tmp_path = tmp.name
    notekeeper._save_notes([], tmp_path)
    yield tmp_path
    os.unlink(tmp_path)

def test_criterion_1_notekeeper_module_exists():
    import notekeeper
    assert hasattr(notekeeper, 'add_note')
    assert hasattr(notekeeper, 'get_notes')
    assert hasattr(notekeeper, 'delete_note')

def test_criterion_2_add_note_saves(temp_storage):
    notekeeper.add_note("Test Note", temp_storage)
    with open(temp_storage, 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]['content'] == "Test Note"

def test_criterion_3_get_notes_retrieves(temp_storage):
    notekeeper.add_note("Note 1", temp_storage)
    notekeeper.add_note("Note 2", temp_storage)
    notes = notekeeper.get_notes(temp_storage)
    assert len(notes) == 2
    assert notes[0]['content'] == "Note 1"
    assert notes[1]['content'] == "Note 2"

def test_criterion_4_delete_note_removes(temp_storage):
    notekeeper.add_note("To Delete", temp_storage)
    notekeeper.add_note("Keep", temp_storage)
    notekeeper.delete_note("1", temp_storage)
    notes = notekeeper.get_notes(temp_storage)
    assert len(notes) == 1
    assert notes[0]['content'] == "Keep"

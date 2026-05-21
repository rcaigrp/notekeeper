import os
import json
import pytest
import tempfile
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import notekeeper

@pytest.fixture
def temp_storage():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as f:
        path = f.name
    notekeeper.set_storage_path(path)
    yield path
    os.remove(path)

def test_criterion_1_notekeeper_module_exists():
    import notekeeper
    assert notekeeper is not None

def test_criterion_2_add_note_saves_to_storage(temp_storage):
    result = notekeeper.add_note("Title", "Content")
    assert result["id"] == "1"
    assert result["title"] == "Title"
    assert result["content"] == "Content"
    with open(temp_storage) as f:
        data = json.load(f)
    assert len(data) == 1

def test_criterion_3_get_notes_retrieves_all(temp_storage):
    notekeeper.add_note("T1", "C1")
    notekeeper.add_note("T2", "C2")
    notes = notekeeper.get_notes()
    assert len(notes) == 2

def test_criterion_4_delete_note_removes_specific(temp_storage):
    notekeeper.add_note("T1", "C1")
    notekeeper.add_note("T2", "C2")
    assert notekeeper.delete_note("1") == True
    notes = notekeeper.get_notes()
    assert len(notes) == 1
    assert notes[0]["id"] == "2"

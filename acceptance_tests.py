import sys
import os
import pytest
import tempfile

sys.path.insert(0, '/workspace/projects/NoteKeeper')

import notekeeper

@pytest.fixture
def reset_storage():
    original_file = notekeeper.STORAGE_FILE
    fd, path = tempfile.mkstemp()
    os.close(fd)
    notekeeper.STORAGE_FILE = path
    yield
    notekeeper.STORAGE_FILE = original_file
    if os.path.exists(path):
        os.remove(path)

def test_criterion_1_module_exists():
    assert hasattr(notekeeper, 'add_note')
    assert hasattr(notekeeper, 'get_notes')
    assert hasattr(notekeeper, 'delete_note')

def test_criterion_2_add_note(reset_storage):
    notekeeper.add_note("Test Note")
    notes = notekeeper.get_notes()
    assert len(notes) == 1
    assert notes[0]["text"] == "Test Note"

def test_criterion_3_get_notes(reset_storage):
    notekeeper.add_note("Note 1")
    notekeeper.add_note("Note 2")
    notes = notekeeper.get_notes()
    assert len(notes) == 2

def test_criterion_4_delete_note(reset_storage):
    notekeeper.add_note("To Delete")
    notekeeper.delete_note(1)
    notes = notekeeper.get_notes()
    assert len(notes) == 0

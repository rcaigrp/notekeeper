import os
import pytest

STORAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json")

@pytest.fixture(autouse=True)
def clean_storage():
    if os.path.exists(STORAGE_PATH):
        os.remove(STORAGE_PATH)
    yield
    if os.path.exists(STORAGE_PATH):
        os.remove(STORAGE_PATH)

def test_criterion_1_import():
    import notekeeper
    assert True

def test_criterion_2_add_note():
    import notekeeper
    assert notekeeper.add_note("1", "content") == True
    assert os.path.exists(STORAGE_PATH)

def test_criterion_3_get_notes():
    import notekeeper
    notekeeper.add_note("1", "content")
    notes = notekeeper.get_notes()
    assert len(notes) == 1
    assert notes[0]["id"] == "1"

def test_criterion_4_delete_note():
    import notekeeper
    notekeeper.add_note("1", "content")
    notekeeper.add_note("2", "content")
    assert notekeeper.delete_note("1") == True
    notes = notekeeper.get_notes()
    assert len(notes) == 1
    assert notes[0]["id"] == "2"

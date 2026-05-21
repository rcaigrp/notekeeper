import pytest
from unittest.mock import patch, MagicMock
import json
import os


def test_criterion_1_import():
    """Test that notekeeper module exists and can be imported."""
    try:
        import notekeeper
        assert True
    except ImportError:
        assert False


def test_criterion_2_add_note():
    """Test that add_note function saves a note to storage."""
    with patch('os.path.exists', return_value=False):
        with patch('os.path.isfile', return_value=False):
            with patch('builtins.open', MagicMock()) as mock_open:
                mock_open.return_value.__enter__.return_value.write = MagicMock()
                mock_open.return_value.__enter__.return_value.__exit__.return_value = None
                import notekeeper
                result = notekeeper.add_note("Test Note")
                assert result == True


def test_criterion_3_get_notes():
    """Test that get_notes function retrieves all saved notes."""
    with patch('os.path.exists', return_value=True):
        with patch('os.path.isfile', return_value=True):
            mock_json = [{"id": 1, "content": "Test Note"}]
            mock_file = MagicMock()
            mock_file.__enter__.return_value.read.return_value = json.dumps(mock_json)
            mock_file.__enter__.return_value.__exit__.return_value = None
            with patch('builtins.open', return_value=mock_file):
                import notekeeper
                notes = notekeeper.get_notes()
                assert notes == mock_json


def test_criterion_4_delete_note():
    """Test that delete_note function removes a specific note by ID."""
    mock_notes = [{"id": 1, "content": "Test Note"}, {"id": 2, "content": "Other"}]
    with patch('os.path.exists', return_value=True):
        with patch('os.path.isfile', return_value=True):
            mock_file = MagicMock()
            mock_file.__enter__.return_value.read.return_value = json.dumps(mock_notes)
            mock_file.__enter__.return_value.__exit__.return_value = None
            mock_file.__enter__.return_value.write = MagicMock()
            with patch('builtins.open', return_value=mock_file):
                import notekeeper
                result = notekeeper.delete_note(1)
                assert result == True

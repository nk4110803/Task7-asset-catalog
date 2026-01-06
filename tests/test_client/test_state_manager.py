import os
import tempfile
import pytest
from client.state_manager import StateManager
from client.config_manager import ConfigManager

@pytest.fixture
#create a temporary state file for testing
def temp_state_file(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        monkeypatch.setattr(ConfigManager, "DATA_DIR",temp_dir)
        yield temp_dir

def test_new_file_is_changed(temp_state_file):
    filepath = os.path.join(temp_state_file, "new_file.txt")
    with open(filepath, "w") as f:
        f.write("new content")
    state_manager = StateManager()
    assert state_manager.has_changed(filepath) == True

def test_mark_uploaded_prevents_resend(temp_state_file):
    filepath = os.path.join(temp_state_file, "file.txt")
    with open(filepath, "w") as f:
        f.write("existing content")
    state_manager = StateManager()
    state_manager.mark_uploaded(filepath)
    assert state_manager.has_changed(filepath) == False

def test_file_changed_detected(temp_state_file):
    filepath = os.path.join(temp_state_file, "file.txt")
    with open(filepath, "w") as f:
        f.write("initial content")
    state_manager = StateManager()
    state_manager.mark_uploaded(filepath)
    with open(filepath, "w") as f:
        f.write("modified content")
    assert state_manager.has_changed(filepath) == True

def test_state_recovery(temp_state_file):
    filepath = os.path.join(temp_state_file, "file.txt")
    with open(filepath, "w") as f:
        f.write("some content")
    state_manager1 = StateManager()
    state_manager1.mark_uploaded(filepath)
    state_manager2 = StateManager()
    assert state_manager2.has_changed(filepath) == False
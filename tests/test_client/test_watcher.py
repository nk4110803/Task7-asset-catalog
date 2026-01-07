import pytest
from watchdog.events import FileCreatedEvent
from client.watcher import Watcher


class DummyUploader:
    def __init__(self):
        self.uploaded = []

    def upload_file(self, path, state_manager):
        self.uploaded.append(path)
        state_manager.mark_uploaded(path)


def test_watcher_on_created(tmp_path):
    uploader = DummyUploader()

    class DummyState:
        def has_changed(self, path):
            return True

        def mark_uploaded(self, path):
            self.called = path

    state = DummyState()
    watcher = Watcher(str(tmp_path), uploader, state)

    new_file = tmp_path / "new.txt"
    new_file.write_text("test")

    event = FileCreatedEvent(str(new_file))

    watcher.on_created(event)

    assert str(new_file) in uploader.uploaded
    assert getattr(state, "called", None) == str(new_file)

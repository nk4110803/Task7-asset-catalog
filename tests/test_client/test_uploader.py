import pytest
from client.uploader import Uploader
from unittest.mock import patch,Mock

def test_uploader_file(monkeypatch, tmp_path):
    filepath=tmp_path / "file.txt"
    with open(filepath, "w") as f:
        f.write("test content")
    uploader=Uploader()
    mock_post=Mock()
    mock_post.stattus_code=200
    monkeypatch.setattr("requests.post", lambda *a, **kw: mock_post)

    class DummyState:
        def has_changed(self, path):
            return True
        def mark_uploaded(self, path):
            self.called = True
    state=DummyState()
    uploader.upload_file(str(filepath), state)
    assert hasattr(state, "called") and state.called

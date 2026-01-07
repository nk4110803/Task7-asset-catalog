import json
import os
import hashlib
from pathlib import Path
from .config_manager import ConfigManager

class StateManager:
    def __init__(self):
        ConfigManager.ensure_dirs()
        self.state_file = Path(ConfigManager.DATA_DIR) / "state.json"
        try:
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        except FileNotFoundError:
            self.state = {}

    def has_changed(self, filepath) -> bool:
        if not Path(filepath).exists():
            return False
        file_hash = self._compute_hash(filepath)
        prev_hash = self.state.get(filepath)
        return file_hash != prev_hash
    
    def mark_uploaded(self, filepath):
        if not os.path.exists(filepath):
            return
        self.state[filepath] = self._compute_hash(filepath)
        self._save()

    def _compute_hash(self, filepath) -> str:
        with open(filepath, "rb") as f:
            data=f.read()
        return hashlib.sha256(data).hexdigest()
    
    def _save(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f)
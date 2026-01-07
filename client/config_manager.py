import os
from pathlib import Path

class ConfigManager:
    DATA_DIR = Path.home() / ".local/share"
    CONFIG_DIR = Path.home() / ".config"
    CACHE_DIR = Path.home() / ".cache"

    @classmethod
    def ensure_dirs(cls):
        cls.DATA_DIR = Path(cls.DATA_DIR)
        print(f"Data directory set to: {cls.DATA_DIR}")
        cls.CONFIG_DIR = Path(cls.CONFIG_DIR)
        cls.CACHE_DIR = Path(cls.CACHE_DIR)
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        cls.CACHE_DIR.mkdir(parents=True, exist_ok=True)

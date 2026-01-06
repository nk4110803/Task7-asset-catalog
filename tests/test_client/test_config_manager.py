from client.config_manager import ConfigManager

def test_directories_created(tmp_path):
    ConfigManager.DATA_DIR=tmp_path / "data"
    ConfigManager.CACHE_DIR=tmp_path / "cache"
    ConfigManager.CONFIG_DIR=tmp_path / "config"
    ConfigManager.ensure_dirs()
    assert ConfigManager.DATA_DIR.exists()
    assert ConfigManager.CONFIG_DIR.exists()
    assert ConfigManager.CACHE_DIR.exists()
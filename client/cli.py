import typer
from client.watcher import Watcher
from client.uploader import Uploader
from client.state_manager import StateManager
from client.config_manager import ConfigManager

app = typer.Typer()

@app.command()
def run(directory: str):
    ConfigManager.ensure_dirs()

    state_manager = StateManager()
    uploader = Uploader()
    watcher = Watcher(directory, uploader, state_manager)
    watcher.start()

if __name__ == "__main__":
    app()

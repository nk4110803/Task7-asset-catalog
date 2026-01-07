import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher(FileSystemEventHandler):
    def __init__(self, directory, uploader, state_manager):
        self.directory = directory
        self.uploader = uploader
        self.state_manager = state_manager

    def scan_existing_files(self):
        print("Performing initial scan...")
        for filename in os.listdir(self.directory):
            full_path = os.path.join(self.directory, filename)
            if os.path.isfile(full_path):
                self.uploader.upload_file(full_path, self.state_manager)

    def start(self,blocking=True):
        self.scan_existing_files()
        observer = Observer()
        observer.schedule(self, self.directory, recursive=False)
        observer.start()

        print(f"Watching directory: {self.directory}")
        if not blocking:
            return observer
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def on_created(self, event):
        if event.is_directory:
            return
        path = self._extract_path_from_event(event)
        if path:
            self.uploader.upload_file(path, self.state_manager)

    def on_modified(self, event):
        if event.is_directory:
            return
        path = self._extract_path_from_event(event)
        if path:
            self.uploader.upload_file(path, self.state_manager)

    def _extract_path_from_event(self, event):
        for attr in ("src_path", "dest_path", "pathname", "path"):
            val = getattr(event, attr, None)
            if isinstance(val, str):
                return val
        try:
            return str(event)
        except Exception:
            return None

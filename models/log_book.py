import json
from .log_entry import LogEntry

class LogBook:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def delete_entry(self, idx):
        if 0 <= idx < len(self.entries):
            del self.entries[idx]

    def change_status(self, idx):
        if 0 <= idx < len(self.entries):
            entry = self.entries[idx]
            entry.status = "DONE" if entry.status == "OPEN" else "OPEN"

    def search(self, keyword):
        keyword = keyword.lower()
        return [e for e in self.entries if keyword in e.title.lower() or keyword in e.description.lower()]

    def filter_by_status(self, status):
        return [e for e in self.entries if e.status == status.upper()]

    def save_to_file(self, filename="logbook.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.entries], f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename="logbook.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.entries = [LogEntry.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []

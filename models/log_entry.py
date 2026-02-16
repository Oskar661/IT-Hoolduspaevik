from datetime import datetime

class LogEntry:
    def __init__(self, title, description, status="OPEN", created_at=None):
        if not title or len(title.strip()) < 4:
            raise ValueError("Pealkiri peab olema vähemalt 4 tähemärki!")
        if not description or len(description.strip()) < 10:
            raise ValueError("Kirjeldus peab olema vähemalt 10 tähemärki!")

        self.title = title.strip()
        self.description = description.strip()
        self.status = status.upper() if status.upper() in ["OPEN", "DONE"] else "OPEN"
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return LogEntry(
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status", "OPEN"),
            created_at=data.get("created_at")
        )

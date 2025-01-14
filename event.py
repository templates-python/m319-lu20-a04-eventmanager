"""
Dataclass Event.py
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:

    title: str
    start: datetime
    end: datetime

    @property
    def duration(self):
        """
        Gibt die Differenz zwischen end und start als timedelta zurück.
        """
        return self.end - self.start
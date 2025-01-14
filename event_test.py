import pytest
from datetime import datetime
from event import Event

def test_event_creation():
    start = datetime(2023, 1, 10, 9, 0, 0)
    end = datetime(2023, 1, 10, 17, 0, 0)
    event = Event("Sample Event", start, end)

    assert event.title == "Sample Event"
    assert event.start == start
    assert event.end == end

def test_event_duration_days():
    start = datetime(2023, 1, 1, 0, 0, 0)
    end = datetime(2023, 1, 3, 0, 0, 0)
    event = Event("Multi-day Event", start, end)
    # Dauer sollte 2 Tage sein
    assert event.duration == 2

def test_event_duration_hours():
    start = datetime(2023, 1, 1, 10, 0, 0)
    end = datetime(2023, 1, 1, 18, 0, 0)
    event = Event("Single-day Event", start, end)
    # Dauer könnte z.B. als 8 Stunden interpretiert werden
    assert event.duration == 8
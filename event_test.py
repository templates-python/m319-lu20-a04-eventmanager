import pytest
from datetime import datetime, timedelta
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
    # Erwartete Differenz: 2 volle Tage
    assert event.duration == timedelta(days=2)

def test_event_duration_hours():
    start = datetime(2023, 1, 1, 10, 0, 0)
    end = datetime(2023, 1, 1, 18, 0, 0)
    event = Event("Single-day Event", start, end)
    # Erwartete Differenz: 8 Stunden
    assert event.duration == timedelta(hours=8)
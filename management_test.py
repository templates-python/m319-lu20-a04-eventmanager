import pytest
from datetime import datetime, timedelta
from management import create_event, show_events, main

def test_create_event(monkeypatch):
    inputs = iter([
        "Test Event",
        "01.01.2023 10:00",  # Startdatum
        "01.01.2023 12:00",  # Enddatum
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event = create_event()

    assert event.title == "Test Event"
    assert event.start == datetime(2023, 1, 1, 10, 0)
    assert event.end == datetime(2023, 1, 1, 12, 0)
    # Überprüfung von timedelta (2 Stunden)
    assert event.duration == timedelta(hours=2)

def test_show_events(capsys):
    from event import Event
    e1 = Event("Event 1", datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 12, 0))
    e2 = Event("Event 2", datetime(2023, 1, 2, 8, 0), datetime(2023, 1, 2, 10, 30))
    events = [e1, e2]
    show_events(events)
    captured = capsys.readouterr()

    assert "Event 1" in captured.out
    assert "Event 2" in captured.out
    # Optional könnte man auch den String "12:00:00" oder "2:30:00" prüfen, je nachdem wie man es formatiert.

def test_main_exit(monkeypatch, capsys):
    inputs = iter(["3"])  # Sofort beenden
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Invalid choice!" not in captured.out
import pytest
from datetime import datetime
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

def test_show_events(capsys):
    # Einfacher Test, ob show_events etwas ausgibt
    from event import Event
    e1 = Event("Event 1", datetime(2023, 1, 1), datetime(2023, 1, 2))
    e2 = Event("Event 2", datetime(2023, 1, 3), datetime(2023, 1, 4))
    events = [e1, e2]
    show_events(events)
    captured = capsys.readouterr()
    assert "Event 1" in captured.out
    assert "Event 2" in captured.out

def test_main_exit(monkeypatch, capsys):
    # Testet die Exit-Option
    inputs = iter(["3"])  # Sofort beenden
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    # Wir erwarten keine spezielle Ausgabe, nur dass das Programm sofort endet
    # Hier könnte man aber prüfen, ob "Invalid choice!" nicht auftaucht, etc.
    assert "Invalid choice!" not in captured.out
import pytest
from datetime import datetime, timedelta
from management import create_event, show_events, main, read_date


def test_read_date_valid(monkeypatch):
    """
    Testet, ob read_date ein korrekt formatiertes Datum (dd.mm.yyyy hh:mm)
    fehlerfrei einliest und als datetime zurückgibt.
    """
    # Wir simulieren einen Nutzer, der zuerst '10.02.2025 18:00' eingibt
    inputs = iter(["10.02.2025 18:00"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    dt = read_date("Enter date/time: ")
    assert dt == datetime(2025, 2, 10, 18, 0)


def test_read_date_invalid(monkeypatch, capsys):
    """
    Testet, ob read_date bei ungültigem Format eine Fehlermeldung ausgibt
    und dann die Eingabe erneut abfragt.
    """
    # Zuerst ein ungültiges Format, danach ein korrektes
    inputs = iter(["not a date", "10.02.2025 18:00"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    dt = read_date("Enter date/time: ")
    captured = capsys.readouterr()

    # Prüfen, ob die Fehlermeldung kam
    assert "Invalid date/time format. Please try again." in captured.out
    # Beim zweiten Versuch sollte es klappen
    assert dt == datetime(2025, 2, 10, 18, 0)


def test_create_event(monkeypatch):
    """
    Testet, ob create_event() das Event korrekt anlegt,
    inkl. Prüfung auf das eingelesene Datum via read_date().
    """
    inputs = iter([
        "Test Event",
        "01.01.2023 10:00",  # Gültiges Startdatum
        "01.01.2023 12:00",  # Gültiges Enddatum
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    event = create_event()

    assert event.title == "Test Event"
    assert event.start == datetime(2023, 1, 1, 10, 0)
    assert event.end == datetime(2023, 1, 1, 12, 0)
    assert event.duration == timedelta(hours=2)


def test_show_events(capsys):
    """
    Testet, ob show_events() die Events korrekt im Terminal ausgibt.
    """
    from event import Event
    e1 = Event("Event 1", datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 1, 12, 0))
    e2 = Event("Event 2", datetime(2023, 1, 2, 8, 0), datetime(2023, 1, 2, 10, 30))
    events = [e1, e2]
    show_events(events)
    captured = capsys.readouterr()

    assert "Event 1" in captured.out
    assert "Event 2" in captured.out
    # Optional: Genauere Prüfung der Duration-/Datums-Strings


def test_main_exit(monkeypatch, capsys):
    """
    Testet, ob main() bei Eingabe '3' direkt beendet,
    ohne Fehlermeldung.
    """
    inputs = iter(["3"])  # Sofort beenden
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()

    # "Invalid choice!" sollte nicht erscheinen
    assert "Invalid choice!" not in captured.out
    assert "Exiting the program. Goodbye!" in captured.out

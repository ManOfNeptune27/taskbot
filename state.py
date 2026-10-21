import json
from datetime import datetime
from pathlib import Path

SENT_FILE = Path.home() / ".taskbot" / "sent_state.json"


def load():
    if not SENT_FILE.exists():
        return {}
    return json.loads(SENT_FILE.read_text())


def last_sent(key):
    value = load().get(key)
    if value is None:
        return None
    return datetime.fromisoformat(value)


def sent_today(key):
    last = last_sent(key)
    return last is not None and last.date() == datetime.now().date()

def mark_sent(key):
    data = load()
    data[key] = datetime.now().isoformat()
    SENT_FILE.parent.mkdir(exist_ok=True)
    SENT_FILE.write_text(json.dumps(data))


def is_due(key, every_hours):
    last = last_sent(key)
    if last is None:
        return True
    elapsed = (datetime.now() - last).total_seconds() / 3600
    return elapsed >= every_hours


def in_active_hours(start, end):
    return start <= datetime.now().hour < end

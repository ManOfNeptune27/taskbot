import re
from datetime import date
from pathlib import Path

from notify import notify
from state import is_due, in_active_hours, mark_sent

TODO_FILE = Path.home() / ".todo-txt" / "todo.txt"
WARN_DAYS = 1
REMIND_EVERY_HOURS = 3
ACTIVE_START = 9
ACTIVE_END = 21

def read_task():
    if not TODO_FILE.exists():
        return []
    return TODO_FILE.read_text().splitlines()


def parse_due(line):
    match = re.search(r"due:(\d{4}-\d{2}-\d{2})", line)
    if match is None:
        return None
    return date.fromisoformat(match.group(1))


def due_status(due, today):
    days_left = (due - today).days
    if days_left < 0:
        return "OVERDUE"
    if days_left == 0:
        return "DUE TODAY"
    if days_left <= WARN_DAYS:
        return "Due soon"
    return None


def check():
    if not in_active_hours(ACTIVE_START, ACTIVE_END):
        return
    today = date.today()
    alerts = []
    keys = []
    for line in read_task():
        if line.startswith("x "):
            continue
        due = parse_due(line)
        if due is None:
            continue
        status = due_status(due, today)
        if status is None:
            continue
        key = f"todo:{status}:{line}"
        if not is_due(key, REMIND_EVERY_HOURS):
            continue
        alerts.append(f"{status}: {line}")
        keys.append(key)
    if alerts:
        message = "\n".join(alerts)
        print(message)
        notify(message, title="Todo")
        for key in keys:
            mark_sent(key)

def main():
    check()


if __name__ == "__main__":
    main()

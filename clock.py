import json
import sys
from datetime import datetime
from pathlib import Path

STATE_FILE = Path.home() / ".taskbot" / "clock_state.json"

def read_start():
    if not STATE_FILE.exists():
        return None
    data = json.loads(STATE_FILE.read_text())
    return datetime.fromisoformat(data["start"])

def format_elapsed(delta):
    total_minutes = int(delta.total_seconds() // 60)
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours}h {minutes}m"


def start():
    if read_start() is not None:
        print("Already clocked in.")
        return
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps({"start": datetime.now().isoformat()}))
    print("Clocked in.")

def status():
    started = read_start()
    if started is None:
        print("Not clocked in.")
        return
    elapsed = datetime.now() - started
    print(f"Clocked in for {format_elapsed(elapsed)}.")


def main():
    if len(sys.argv) < 2:
        print("Usage: clock.py start|status")
        return

    command = sys.argv[1]
    if command == "start":
        start()
    elif command == "status":
        status()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

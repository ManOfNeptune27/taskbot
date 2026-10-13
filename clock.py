import json
import sys
from datetime import datetime
from pathlib import Path

STATE_FILE = Path.home() / ".taskbot" / "clock_state.json"


def start():
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps({"start": datetime.now().isoformat()}))
    print("Clocked in.")


def main():
    if len(sys.argv) < 2:
        print("Usage: clock.py start")
        return

    command = sys.argv[1]
    if command == "start":
        start()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

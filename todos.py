import re 
from datetime import date
from pathlib import Path

TODO_FILE = Path.home() / ".todo-txt" / "todo.txt"


def read_task():
    if not TODO_FILE.exists():
        return []
    return TODO_FILE.read_text().splitlines()

def parse_due(line):
    match = re.search(r"due:(\d{4}-\d{2}-\d{2})", line)
    if match is None:
        return None
    return date.fromisoformat(match.group(1))

def main():
    for line in read_task():
        if line.startswith("x "):
            continue
        due = parse_due(line)
        if due is not None:
            print(due, line)

if __name__ == "__main__":
    main()

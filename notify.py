import urllib.request
from pathlib import Path

TOPIC_FILE = Path.home() / ".taskbot" / "ntfy_topic"


def get_topic():
    return TOPIC_FILE.read_text().strip()


def notify(message, title="taskbot"):
    url = f"https://ntfy.sh/{get_topic()}"
    request = urllib.request.Request(
        url,
        data=message.encode("utf-8"),
        headers={"Title": title}
    )
    urllib.request.urlopen(request, timeout=10)


if __name__ == "__main__":
    notify("Test from Taskbot")

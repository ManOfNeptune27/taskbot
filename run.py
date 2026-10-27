import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from clock import ping
from todos import check
from water import remind

LOG_FILE = Path.home() / ".taskbot" / "taskbot.log"


def setup_logging():
    LOG_FILE.parent.mkdir(exist_ok=True)
    handler = RotatingFileHandler(LOG_FILE, maxBytes=100_000, backupCount=2)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[handler],
    )


def run_step(name, step):
    try:
        step()
        logging.info("%s ok", name)
    except Exception:
        logging.exception("%s failed", name)


def main():
    setup_logging()
    logging.info("run started")
    run_step("clock ping", ping)
    run_step("todo check", check)
    run_step("water reminder", remind)


if __name__ == "__main__":
    main()

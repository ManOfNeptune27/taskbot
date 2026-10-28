# taskbot

A small personal bot that keeps me on task with phone notifications.
Written in plain Python (standard library only) as a learning project.

## Features

- **Clock tracker**: `clock.py` records when I clock in and out and reports elapsed time.
- **Todo reminders**: reads a todo.txt file and sends alerts for tasks that are due soon or overdue, repeating on an interval during active hours.
- **Water reminders**: periodic nudges to drink water during set hours.
- **Phone notifications**: everything is delivered through [ntfy](https://ntfy.sh).
- **Logging**: every scheduled run is recorded in a rotating log file.

## Requirements

- Python 3 (no third-party packages)
- The [todo.txt CLI](https://github.com/todotxt/todo.txt-cli)
- The ntfy app on your phone

## Setup

1. Clone the repo.
2. Pick a long, random ntfy topic, subscribe to it in the ntfy app, and save it outside the repo:

   ```bash
   mkdir -p ~/.taskbot
   echo "your-random-topic" > ~/.taskbot/ntfy_topic
   ```

3. Send a test notification: `python3 notify.py`

## Usage

```bash
python3 clock.py start     # clock in
python3 clock.py status    # how long you've been clocked in
python3 clock.py stop      # clock out
python3 run.py             # run every check once
```

Tasks with due dates use the todo.txt convention, for example:
`(A) Submit application due:2026-10-30`

## Configuration

Settings are constants at the top of each file:

- `todos.py`: `WARN_DAYS`, `REMIND_EVERY_HOURS`, `ACTIVE_START`, `ACTIVE_END`
- `water.py`: `WATER_EVERY_HOURS`, `WATER_START`, `WATER_END`

## Scheduling

`run.py` is meant to run every 15 minutes. I use Windows Task Scheduler
calling it through WSL, but cron or a systemd timer works the same way.
Logs are written to `~/.taskbot/taskbot.log`.

## Privacy

The ntfy topic and all state files live in `~/.taskbot/`, outside the repo.
Never commit your topic name, since anyone who knows it can read your notifications.

## License

MIT

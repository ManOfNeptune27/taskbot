from notify import notify
from state import is_due, in_active_hours, mark_sent

WATER_EVERY_HOURS = 2
WATER_START = 9
WATER_END = 17
GRACE_HOURS = 0.1
KEY = "water"

def remind():
    if not in_active_hours(WATER_START, WATER_END):
        return
    if not is_due(KEY, WATER_EVERY_HOURS - GRACE_HOURS):
        return
    notify("Time to drink some water.", title="Water")
    mark_sent(KEY)

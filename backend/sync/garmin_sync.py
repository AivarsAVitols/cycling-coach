"""
Garmin → Supabase sync script.
Run via Windows Task Scheduler or manually:  python -m backend.sync.garmin_sync
Milestone 2 will fill in the full implementation.
"""

import os
import sys
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()


def sync(days_back: int = 7) -> None:
    raise NotImplementedError("Milestone 2: implement Garmin sync")


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    sync(days)

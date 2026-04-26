"""
Training metrics module.
Computes per-activity metrics and updates health_daily CTL/ATL/TSB.
Milestone 3 will fill in the full implementation.
"""


def compute_activity_metrics(power_stream: list[float], hr_stream: list[float], ftp: float) -> dict:
    raise NotImplementedError("Milestone 3: implement metrics computation")


def update_fitness_metrics() -> None:
    """Recompute CTL, ATL, TSB for all dates and upsert into health_daily."""
    raise NotImplementedError("Milestone 3: implement fitness metric roll-up")

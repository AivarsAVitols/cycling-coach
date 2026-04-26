# Training Guidelines

> **Status: placeholder** — generate the real content in a dedicated Claude Code session (milestone 4).
>
> Prompt to use: "Generate a comprehensive cycling training rulebook covering periodization,
> polarized vs pyramidal intensity distribution, taper protocols, recovery thresholds, and
> workout templates keyed to goals like 3-min power, aerobic base, and durability >2 hours."

This file is the canonical knowledge source for `backend/planner/rules_engine.py`.
It should cover:

- Periodization models (base → build → peak → taper)
- Intensity zones (power-based, 7-zone model referenced to FTP)
- Polarized vs pyramidal distribution and when to use each
- Weekly TSS targets by phase and CTL level
- Recovery rules (TSB thresholds for hard/easy/rest days)
- HRV / resting HR flags that trigger plan adjustments
- Workout templates: VO2max, threshold, sweet-spot, endurance, recovery
- Goal-specific focus: 3-min power, aerobic base, durability >2 h
- Taper protocol for A-race vs B-race
- FTP estimation heuristic (if no manual override)

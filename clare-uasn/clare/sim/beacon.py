"""Beacon schedule from Eq. (2) of Section III-A-2."""
from __future__ import annotations
from clare.core.collision import beacon_slot, interference_free, DT_SLOT


def schedule(m=4, t0=0.0, dt_slot=DT_SLOT):
    """Return the list of beacon times for M AUVs."""
    return [beacon_slot(t0, i, dt_slot) for i in range(1, m + 1)]


def all_slots_free(times, d_max=1500.0, c0=1500.0):
    """Check Eq. (3) across all pairs."""
    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            if not interference_free(times[i], times[j], d_max, c0):
                return False
    return True

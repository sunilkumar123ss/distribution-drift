"""Descriptive numeric drift: fixed-bin PSI, empirical KS distance, mean shift."""
import argparse
import bisect
import json
from pathlib import Path
import math
import statistics
import sys


def finite_list(values, name, minimum=1):
    if not isinstance(values, list) or len(values) < minimum:
        raise ValueError(f"{name} must be a list with at least {minimum} values")
    if any(type(x) not in (int, float) or not math.isfinite(x) for x in values):
        raise ValueError(f"{name} must contain finite numbers")


def evaluate(baseline, current, edges, smoothing=0.5):
    finite_list(baseline, "baseline", 2)
    finite_list(current, "current", 2)
    finite_list(edges, "edges")
    if any(a >= b for a, b in zip(edges, edges[1:])):
        raise ValueError("edges must be strictly increasing")
    if type(smoothing) not in (int, float) or not math.isfinite(smoothing) or smoothing <= 0:
        raise ValueError("smoothing must be positive and finite")
    counts = []
    for values in (baseline, current):
        row = [0] * (len(edges) + 1)
        for value in values:
            row[bisect.bisect_right(edges, value)] += 1
        counts.append(row)
    proportions = [[(count + smoothing) / (sum(row) + smoothing * len(row)) for count in row] for row in counts]
    psi = sum((q - p) * math.log(q / p) for p, q in zip(*proportions))
    base, new = sorted(baseline), sorted(current)
    ks = max(abs(bisect.bisect_right(base, point) / len(base) -
                 bisect.bisect_right(new, point) / len(new)) for point in set(base + new))
    stdev = statistics.pstdev(baseline)
    return {"baseline_counts": counts[0], "current_counts": counts[1],
            "smoothed_psi": psi, "ks_distance": ks,
            "baseline_mean": statistics.mean(baseline), "current_mean": statistics.mean(current),
            "mean_shift_baseline_std": (statistics.mean(current) - statistics.mean(baseline)) / stdev if stdev else None,
            "smoothing_pseudocount": smoothing}


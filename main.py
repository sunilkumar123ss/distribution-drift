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


import unittest
from main import evaluate


class DriftTests(unittest.TestCase):
    def test_identical_distribution(self):
        result = evaluate([0, 1, 2, 3], [3, 2, 1, 0], [1, 2])
        self.assertEqual(result["smoothed_psi"], 0)
        self.assertEqual(result["ks_distance"], 0)
        self.assertEqual(result["baseline_counts"], [1, 1, 2])


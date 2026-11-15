import subprocess
import sys
import unittest
from pathlib import Path


PROGRAM = Path(__file__).resolve().parents[1] / "main.py"


class MainTests(unittest.TestCase):
    def test_integer_coefficients_are_printed_with_the_discriminant(self):
        result = subprocess.run(
            [sys.executable, str(PROGRAM)],
            input="1\n-3\n2\n",
            text=True,
            capture_output=True,
            check=True,
        )

        self.assertIn("a = 1.0, b = -3.0, c = 2.0", result.stdout)
        self.assertIn("Дискриминант D = 1.0", result.stdout)

    def test_fractional_coefficients_are_used_in_the_calculation(self):
        result = subprocess.run(
            [sys.executable, str(PROGRAM)],
            input="-0.5\n1.5\n2\n",
            text=True,
            capture_output=True,
            check=True,
        )

        self.assertIn("a = -0.5, b = 1.5, c = 2.0", result.stdout)
        self.assertIn("Дискриминант D = 6.25", result.stdout)

    def test_negative_discriminant_is_printed(self):
        result = subprocess.run(
            [sys.executable, str(PROGRAM)],
            input="1\n2\n3\n",
            text=True,
            capture_output=True,
            check=True,
        )

        self.assertIn("Дискриминант D = -8.0", result.stdout)

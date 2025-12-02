# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from pandasreporter import PandasReporter


class TestConstructor(unittest.TestCase):

    def test_constructor(self):
        reporter = PandasReporter()
        self.assertIsInstance(reporter, PandasReporter)

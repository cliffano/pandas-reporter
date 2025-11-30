# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from pandasreporter import PandasReporter


class TestConstructor(unittest.TestCase):

    def test_constructor(self):
        reporter = PandasReporter(out_format="html", max_col_size=80)
        assert reporter.out_format == "html"

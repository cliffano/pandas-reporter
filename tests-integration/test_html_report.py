# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
import asyncio
import pandas as pd
from pandasreporter import PandasReporter

# Silence dominaate 'There is no current event loop' warning
asyncio.set_event_loop(asyncio.new_event_loop())


class TestHtmlReport(unittest.TestCase):

    def test_html_report_to_stdout(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {
            "title": "Some Report",
            "generator": "Some Generator",
            "rows_styler": lambda x: [""] * len(x),
            "max_col_size": 80,
        }

        pandas_reporter.report(
            data_frame,
            "html",
            _opts,
        )

    def test_html_report_to_file(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {
            "title": "Some Report",
            "generator": "Some Generator",
            "rows_styler": lambda x: [""] * len(x),
            "max_col_size": 80,
            "out_file": "stage/test-integration/test_html_report_output.html",
        }

        pandas_reporter.report(
            data_frame,
            "html",
            _opts,
        )

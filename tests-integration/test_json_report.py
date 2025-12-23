# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
import pandas as pd
from pandasreporter import PandasReporter


class TestJsonReport(unittest.TestCase):

    def test_json_report_to_stdout(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {}

        pandas_reporter.report(
            data_frame,
            "json",
            _opts,
        )

    def test_json_report_to_file(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {
            "out_file": "stage/test-integration/test_json_report_output.html",
        }

        pandas_reporter.report(
            data_frame,
            "json",
            _opts,
        )

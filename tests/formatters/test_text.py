# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
import pandas as pd
from pandasreporter.formatters.text import format_report


class TestTextFormatter(unittest.TestCase):

    def test_format_report_with_empty_data(self):
        data = {}
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected = ""
        self.assertEqual(result, expected)

    def test_format_report_with_simple_data(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected = (
            "┌──────────┬──────────┬──────────────┐\n"
            "│ Name     │      DOB │ City         │\n"
            "├──────────┼──────────┼──────────────┤\n"
            "│ Barkley  │ 19630220 │ Philadelphia │\n"
            "├──────────┼──────────┼──────────────┤\n"
            "│ Pippen   │ 19650925 │ Chicago      │\n"
            "├──────────┼──────────┼──────────────┤\n"
            "│ Robinson │ 19650806 │ San Antonio  │\n"
            "└──────────┴──────────┴──────────────┘"
        )
        self.assertEqual(result, expected)

    def test_format_report_with_nested_data(self):
        data = {
            "Players": {
                "Barkley": {"DOB": "19630220", "City": "Philadelphia"},
                "Pippen": {"DOB": "19650925", "City": "Chicago"},
                "Robinson": {"DOB": "19650806", "City": "San Antonio"},
            }
        }
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected = (
            "┌─────────────────────────────────────────────┐\n"
            "│ Players                                     │\n"
            "├─────────────────────────────────────────────┤\n"
            "│ {'DOB': '19630220', 'City': 'Philadelphia'} │\n"
            "├─────────────────────────────────────────────┤\n"
            "│ {'DOB': '19650925', 'City': 'Chicago'}      │\n"
            "├─────────────────────────────────────────────┤\n"
            "│ {'DOB': '19650806', 'City': 'San Antonio'}  │\n"
            "└─────────────────────────────────────────────┘"
        )
        self.assertEqual(result, expected)

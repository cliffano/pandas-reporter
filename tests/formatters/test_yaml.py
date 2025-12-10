# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
import pandas as pd
from pandasreporter.formatters.yaml_ import format_report


class TestYamlFormatter(unittest.TestCase):

    def test_format_report_with_empty_data(self):
        data = {}
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected = (
            "[]\n"
        )
        self.assertEqual(result, expected)

    def test_format_report_with_simple_data(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        print(result)
        expected = (
            '- City: Philadelphia\n'
            '  DOB: \'19630220\'\n'
            '  Name: Barkley\n'
            '- City: Chicago\n'
            '  DOB: \'19650925\'\n'
            '  Name: Pippen\n'
            '- City: San Antonio\n'
            '  DOB: \'19650806\'\n'
            '  Name: Robinson\n'
        )
        self.assertEqual(result, expected)

    # def test_format_report_with_nested_data(self):
    #     data = {
    #         "Players": {
    #             "Barkley": {"DOB": "19630220", "City": "Philadelphia"},
    #             "Pippen": {"DOB": "19650925", "City": "Chicago"},
    #             "Robinson": {"DOB": "19650806", "City": "San Antonio"},
    #         }
    #     }
    #     data_frame = pd.DataFrame(data)
    #     result = format_report(data_frame, {})
    #     print(result)
    #     expected = (
    #         '[\n'
    #         '  {\n'
    #         '    "Players":{\n'
    #         '      "DOB":"19630220",\n'
    #         '      "City":"Philadelphia"\n'
    #         '    }\n'
    #         '  },\n'
    #         '  {\n'
    #         '    "Players":{\n'
    #         '      "DOB":"19650925",\n'
    #         '      "City":"Chicago"\n'
    #         '    }\n'
    #         '  },\n'
    #         '  {\n'
    #         '    "Players":{\n'
    #         '      "DOB":"19650806",\n'
    #         '      "City":"San Antonio"\n'
    #         '    }\n'
    #         '  }\n'
    #         ']'
    #     )
    #     self.assertEqual(result, expected)

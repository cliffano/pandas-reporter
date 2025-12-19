# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals,line-too-long
import unittest
import pandas as pd
from pandasreporter.formatters.html import format_report


class TestHtmlFormatter(unittest.TestCase):

    def test_format_report_with_empty_data(self):
        data = {}
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected_pattern = (
            r"<!DOCTYPE html>\n"
            r"<html>\n"
            r"  <head>\n"
            r"    <title>Pandas Report</title>\n"
            r'    <meta charset="utf-8">\n'
            r'    <meta content="Pandas Reporter" name="generator">\n'
            r'    <link href="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.6/dist/css/bootstrap\.min\.css" rel="stylesheet">\n'
            r"  </head>\n"
            r'  <body><style type="text/css">\n'
            r"</style>\n"
            r'<table id="T_[a-f0-9]+" class="table table-striped table-bordered table-hover">\n'
            r"  <thead>\n"
            r"  </thead>\n"
            r"  <tbody>\n"
            r"  </tbody>\n"
            r"</table>\n"
            r"</body>\n"
            r"</html>"
        )

        self.assertRegex(result, expected_pattern)

    def test_format_report_with_simple_data(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)
        result = format_report(data_frame, {})
        expected_pattern = (
            r"<!DOCTYPE html>\n"
            r"<html>\n"
            r"  <head>\n"
            r"    <title>Pandas Report</title>\n"
            r'    <meta charset="utf-8">\n'
            r'    <meta content="Pandas Reporter" name="generator">\n'
            r'    <link href="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.6/dist/css/bootstrap\.min\.css" rel="stylesheet">\n'
            r"  </head>\n"
            r'  <body><style type="text/css">\n'
            r"</style>\n"
            r'<table id="T_[a-f0-9]+" class="table table-striped table-bordered table-hover">\n'
            r"  <thead>\n"
            r"    <tr>\n"
            r'      <th class="blank level0" >&nbsp;</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col0" class="text-center table-active col_heading level0 col0" >Name</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col1" class="text-center table-active col_heading level0 col1" >DOB</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col2" class="text-center table-active col_heading level0 col2" >City</th>\n'
            r"    </tr>\n"
            r"  </thead>\n"
            r"  <tbody>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row0" class="row_heading level0 row0" >0</th>\n'
            r'      <td id="T_[a-f0-9]+_row0_col0" class="data row0 col0" >Barkley</td>\n'
            r'      <td id="T_[a-f0-9]+_row0_col1" class="data row0 col1" >19630220</td>\n'
            r'      <td id="T_[a-f0-9]+_row0_col2" class="data row0 col2" >Philadelphia</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row1" class="row_heading level0 row1" >1</th>\n'
            r'      <td id="T_[a-f0-9]+_row1_col0" class="data row1 col0" >Pippen</td>\n'
            r'      <td id="T_[a-f0-9]+_row1_col1" class="data row1 col1" >19650925</td>\n'
            r'      <td id="T_[a-f0-9]+_row1_col2" class="data row1 col2" >Chicago</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row2" class="row_heading level0 row2" >2</th>\n'
            r'      <td id="T_[a-f0-9]+_row2_col0" class="data row2 col0" >Robinson</td>\n'
            r'      <td id="T_[a-f0-9]+_row2_col1" class="data row2 col1" >19650806</td>\n'
            r'      <td id="T_[a-f0-9]+_row2_col2" class="data row2 col2" >San Antonio</td>\n'
            r"    </tr>\n"
            r"  </tbody>\n"
            r"</table>\n"
            r"</body>\n"
            r"</html>"
        )
        self.assertRegex(result, expected_pattern)

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
        expected_pattern = (
            r"<!DOCTYPE html>\n"
            r"<html>\n"
            r"  <head>\n"
            r"    <title>Pandas Report</title>\n"
            r'    <meta charset="utf-8">\n'
            r'    <meta content="Pandas Reporter" name="generator">\n'
            r'    <link href="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.6/dist/css/bootstrap\.min\.css" rel="stylesheet">\n'
            r"  </head>\n"
            r'  <body><style type="text/css">\n'
            r"</style>\n"
            r'<table id="T_[a-f0-9]+" class="table table-striped table-bordered table-hover">\n'
            r"  <thead>\n"
            r"    <tr>\n"
            r'      <th class="blank level0" >&nbsp;</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col0" class="text-center table-active col_heading level0 col0" >Players</th>\n'
            r"    </tr>\n"
            r"  </thead>\n"
            r"  <tbody>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row0" class="row_heading level0 row0" >Barkley</th>\n'
            r'      <td id="T_[a-f0-9]+_row0_col0" class="data row0 col0" >\{\'DOB\': \'19630220\', \'City\': \'Philadelphia\'\}</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row1" class="row_heading level0 row1" >Pippen</th>\n'
            r'      <td id="T_[a-f0-9]+_row1_col0" class="data row1 col0" >\{\'DOB\': \'19650925\', \'City\': \'Chicago\'\}</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row2" class="row_heading level0 row2" >Robinson</th>\n'
            r'      <td id="T_[a-f0-9]+_row2_col0" class="data row2 col0" >\{\'DOB\': \'19650806\', \'City\': \'San Antonio\'\}</td>\n'
            r"    </tr>\n"
            r"  </tbody>\n"
            r"</table>\n"
            r"</body>\n"
            r"</html>"
        )
        self.assertRegex(result, expected_pattern)

    def test_format_report_with_simple_data_and_opts(self):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)
        opts = {
            "title": "Some Title",
            "generator": "Some Generator",
            "colour_rows_styler": lambda x: [""] * len(x),
        }
        result = format_report(data_frame, opts)
        expected_pattern = (
            r"<!DOCTYPE html>\n"
            r"<html>\n"
            r"  <head>\n"
            r"    <title>Some Title</title>\n"
            r'    <meta charset="utf-8">\n'
            r'    <meta content="Some Generator" name="generator">\n'
            r'    <link href="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.6/dist/css/bootstrap\.min\.css" rel="stylesheet">\n'
            r"  </head>\n"
            r'  <body><style type="text/css">\n'
            r"</style>\n"
            r'<table id="T_[a-f0-9]+" class="table table-striped table-bordered table-hover">\n'
            r"  <thead>\n"
            r"    <tr>\n"
            r'      <th class="blank level0" >&nbsp;</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col0" class="text-center table-active col_heading level0 col0" >Name</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col1" class="text-center table-active col_heading level0 col1" >DOB</th>\n'
            r'      <th id="T_[a-f0-9]+_level0_col2" class="text-center table-active col_heading level0 col2" >City</th>\n'
            r"    </tr>\n"
            r"  </thead>\n"
            r"  <tbody>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row0" class="row_heading level0 row0" >0</th>\n'
            r'      <td id="T_[a-f0-9]+_row0_col0" class="data row0 col0" >Barkley</td>\n'
            r'      <td id="T_[a-f0-9]+_row0_col1" class="data row0 col1" >19630220</td>\n'
            r'      <td id="T_[a-f0-9]+_row0_col2" class="data row0 col2" >Philadelphia</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row1" class="row_heading level0 row1" >1</th>\n'
            r'      <td id="T_[a-f0-9]+_row1_col0" class="data row1 col0" >Pippen</td>\n'
            r'      <td id="T_[a-f0-9]+_row1_col1" class="data row1 col1" >19650925</td>\n'
            r'      <td id="T_[a-f0-9]+_row1_col2" class="data row1 col2" >Chicago</td>\n'
            r"    </tr>\n"
            r"    <tr>\n"
            r'      <th id="T_[a-f0-9]+_level0_row2" class="row_heading level0 row2" >2</th>\n'
            r'      <td id="T_[a-f0-9]+_row2_col0" class="data row2 col0" >Robinson</td>\n'
            r'      <td id="T_[a-f0-9]+_row2_col1" class="data row2 col1" >19650806</td>\n'
            r'      <td id="T_[a-f0-9]+_row2_col2" class="data row2 col2" >San Antonio</td>\n'
            r"    </tr>\n"
            r"  </tbody>\n"
            r"</table>\n"
            r"</body>\n"
            r"</html>"
        )
        self.assertRegex(result, expected_pattern)

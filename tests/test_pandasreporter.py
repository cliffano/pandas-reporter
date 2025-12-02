# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from unittest.mock import patch
import unittest
import pandas as pd
from pandasreporter import PandasReporter


class TestPandasReporter(unittest.TestCase):

    @patch("pandasreporter.formatters.html.format_report")
    def test_pandasreporter_format_html(self, mock_format):
        mock_format.return_value = "<html></html>"

        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        with patch.object(PandasReporter, "report", return_value=None) as mock_report:
            pandas_reporter = PandasReporter()
            _opts = {"colour_rows_styler": lambda x: [""] * len(x), "max_col_size": 80}
            pandas_reporter.report(
                data_frame,
                "html",
                opts=_opts,
            )
            mock_report.assert_called_once_with(
                data_frame,
                "html",
                opts=_opts,
            )

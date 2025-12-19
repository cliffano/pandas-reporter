# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from unittest.mock import mock_open, patch
import unittest
import pandas as pd
import pandas.testing as pdt
from pandasreporter import PandasReporter


class TestPandasReporter(unittest.TestCase):

    @patch("pandasreporter.format_html")
    @patch("builtins.print")
    def test_pandasreporter_format_html(self, mock_print, mock_formatter):
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
            "colour_rows_styler": lambda x: [""] * len(x),
            "max_col_size": 80,
        }

        mock_formatter.return_value = "<html></html>"
        pandas_reporter.report(
            data_frame,
            "html",
            _opts,
        )

        mock_formatter.assert_called_once()
        args, kwargs = mock_formatter.call_args
        pdt.assert_frame_equal(args[0], data_frame)
        self.assertEqual(args[1], _opts)

        mock_print.assert_called_once_with("<html></html>")

    @patch("pandasreporter.format_json")
    @patch("builtins.print")
    def test_pandasreporter_format_json(self, mock_print, mock_formatter):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {}

        mock_formatter.return_value = "{}"
        pandas_reporter.report(
            data_frame,
            "json",
            _opts,
        )
        mock_formatter.assert_called_once_with(
            data_frame,
            _opts,
        )
        mock_print.assert_called_once_with("{}")

    @patch("pandasreporter.format_json")
    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_pandasreporter_format_json_with_outfile(self, mock_open_fn, mock_print, mock_formatter):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {"out_file": "output.json"}

        mock_formatter.return_value = "{}"
        pandas_reporter.report(data_frame, "json", _opts)

        mock_formatter.assert_called_once_with(data_frame, _opts)
        mock_open_fn.assert_called_once_with("output.json", "w", encoding="utf-8")
        mock_open_fn().write.assert_called_once_with("{}")
        mock_print.assert_not_called()

    @patch("pandasreporter.format_text")
    @patch("builtins.print")
    def test_pandasreporter_format_text(self, mock_print, mock_formatter):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {}

        mock_formatter.return_value = "some text"
        pandas_reporter.report(
            data_frame,
            "text",
            _opts,
        )
        mock_formatter.assert_called_once_with(
            data_frame,
            _opts,
        )
        mock_print.assert_called_once_with("some text")

    @patch("pandasreporter.format_yaml")
    @patch("builtins.print")
    def test_pandasreporter_format_yaml(self, mock_print, mock_formatter):
        data = {
            "Name": ["Barkley", "Pippen", "Robinson"],
            "DOB": ["19630220", "19650925", "19650806"],
            "City": ["Philadelphia", "Chicago", "San Antonio"],
        }
        data_frame = pd.DataFrame(data)

        pandas_reporter = PandasReporter()
        _opts = {}

        mock_formatter.return_value = "- somefield: somevalue"
        pandas_reporter.report(
            data_frame,
            "yaml",
            _opts,
        )
        mock_formatter.assert_called_once_with(
            data_frame,
            _opts,
        )
        mock_print.assert_called_once_with("- somefield: somevalue")

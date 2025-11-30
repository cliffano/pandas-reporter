# pylint: disable=too-few-public-methods
"""A module for reporting the certificate details
depending on output configurations.
"""

import pandas as pd
from .formatters.html import format_report as format_html
from .formatters.json import format_report as format_json
from .formatters.yaml_ import format_report as format_yaml
from .formatters.text import format_report as format_text


class PandasReporter:
    """A class for producing report from Pandas DataFrame."""

    def __init__(
        self,
        out_format: str,
        max_col_size: int,
    ) -> None:
        """Initialize the PandasReporter object."""
        self.out_format = out_format
        self.max_col_size = max_col_size

    def report(self, data_frame: pd.DataFrame, out_file: str, opts: dict) -> None:
        """Write the data to the output file or stdout."""

        if self.max_col_size:
            data_frame = data_frame.map(
                lambda x: x[0 : self.max_col_size] if isinstance(x, str) else x
            )

        output = self._format_data(data_frame, opts)

        self._write_output(output, out_file)

    def _format_data(self, data_frame, opts) -> str:
        """Format the data frame based on the output format."""
        if self.out_format == "html":
            output = format_html(data_frame, opts)
        elif self.out_format == "json":
            output = format_json(data_frame, opts)
        elif self.out_format == "yaml":
            output = format_yaml(data_frame, opts)
        else:
            output = format_text(data_frame, opts)
        return output

    def _write_output(self, output: str, out_file: str) -> None:
        """Write the output to the file or stdout."""
        if out_file:
            with open(out_file, "w", encoding="utf-8") as (stream):
                stream.write(output)
        else:
            print(output)

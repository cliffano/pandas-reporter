# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from pandasreporter import PandasReporter
import pandas as pd

data = {
    "Name": ["Barkley", "Pippen", "Robinson"],
    "DOB": ["19630220", "19650925", "19650806"],
    "City": ["Philadelphia", "Chicago", "San Antonio"],
}
df = pd.DataFrame(data)

reporter = PandasReporter()

reporter.report(data_frame=df, out_format="text", opts={})
reporter.report(
    data_frame=df,
    out_format="text",
    opts={"out_file": "../stage/test-examples/report.txt"},
)

reporter.report(data_frame=df, out_format="json", opts={})
reporter.report(
    data_frame=df,
    out_format="json",
    opts={"out_file": "../stage/test-examples/report.json"},
)

reporter.report(data_frame=df, out_format="yaml", opts={})
reporter.report(
    data_frame=df,
    out_format="yaml",
    opts={"out_file": "../stage/test-examples/report.yaml"},
)

reporter.report(data_frame=df, out_format="html", opts={})
reporter.report(
    data_frame=df,
    out_format="html",
    opts={"out_file": "../stage/test-examples/report.html"},
)


def _rows_styler(row):
    if row["City"] == "Chicago":
        style = ["background-color: LightPink"] * len(row)
    elif row["City"] == "San Antonio":
        style = ["background-color: LightGreen"] * len(row)
    else:
        style = ["background-color: LightYellow"] * len(row)
    return style


reporter.report(data_frame=df, out_format="html", opts={"rows_styler": _rows_styler})
reporter.report(
    data_frame=df,
    out_format="html",
    opts={
        "rows_styler": _rows_styler,
        "out_file": "../stage/test-examples/report-styled.html",
    },
)

reporter.report(data_frame=df, out_format="html", opts={"max_col_size": 3})
reporter.report(
    data_frame=df,
    out_format="html",
    opts={
        "max_col_size": 3,
        "out_file": "../stage/test-examples/report-maxcolsize.html",
    },
)

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

reporter.report(df, "text", {})
reporter.report(
    df,
    "text",
    {"out_file": "reports/report.txt"},
)

reporter.report(df, "json", {})
reporter.report(
    df,
    "json",
    {"out_file": "reports/report.json"},
)

reporter.report(df, "yaml", {})
reporter.report(
    df,
    "yaml",
    {"out_file": "reports/report.yaml"},
)

reporter.report(df, "html", {})
reporter.report(
    df,
    "html",
    {"out_file": "reports/report.html"},
)


def _rows_styler(row):
    if row["City"] == "Chicago":
        style = ["background-color: LightPink"] * len(row)
    elif row["City"] == "San Antonio":
        style = ["background-color: LightGreen"] * len(row)
    else:
        style = ["background-color: LightYellow"] * len(row)
    return style


reporter.report(df, "html", {"rows_styler": _rows_styler})
reporter.report(
    df,
    "html",
    {
        "rows_styler": _rows_styler,
        "out_file": "reports/report-styled.html",
    },
)

reporter.report(df, "html", {"max_col_size": 3})
reporter.report(
    df,
    "html",
    {
        "max_col_size": 3,
        "out_file": "reports/report-maxcolsize.html",
    },
)

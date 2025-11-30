# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from pandasreporter import Display

display = Display(conf_files=["pandasreporter.yaml"])
text = display.format(reverse=False, transformation="lower")
print(text)

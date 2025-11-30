<img align="right" src="https://raw.github.com/cliffano/pandas-reporter/main/avatar.jpg" alt="Avatar"/>

[![Build Status](https://github.com/cliffano/pandas-reporter/workflows/CI/badge.svg)](https://github.com/cliffano/pandas-reporter/actions?query=workflow%3ACI)
[![Security Status](https://snyk.io/test/github/cliffano/pandas-reporter/badge.svg)](https://snyk.io/test/github/cliffano/pandas-reporter)
[![Dependencies Status](https://img.shields.io/librariesio/release/pypi/pandasreporter)](https://libraries.io/github/cliffano/pandas-reporter)
[![Published Version](https://img.shields.io/pypi/v/pandasreporter.svg)](https://pypi.python.org/pypi/pandasreporter)
<br/>

Pandas Reporter
---------------

Pandas Reporter is a Report builder for Pandas DataFrame .

Installation
------------

    pip3 install pandasreporter

Usage
-----

Create a configuration file, e.g. `pandasreporter.yaml`:

    ---
    text: Hello World

Create pandasreporter object and run it:

    from pandasreporter import Display

    display = Display(conf_files=['pandasreporter.yaml'])
    text = display.format(reverse=False, transformation='lower')
    print(text)

Configuration
-------------

These are the configuration properties that you can use with `pandasreporter` CLI.
Some example configuration files are available on [examples](examples) folder.

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `text` | String | The message text | Hello World |

Colophon
--------

[Developer's Guide](https://cliffano.github.io/developers_guide.html#python)

Build reports:

* [Lint report](https://cliffano.github.io/pandasreporter/lint/pylint/index.html)
* [Code complexity report](https://cliffano.github.io/pandasreporter/complexity/wily/index.html)
* [Unit tests report](https://cliffano.github.io/pandasreporter/test/pytest/index.html)
* [Test coverage report](https://cliffano.github.io/pandasreporter/coverage/coverage/index.html)
* [Integration tests report](https://cliffano.github.io/pandasreporter/test-integration/pytest/index.html)
* [API Documentation](https://cliffano.github.io/pandasreporter/doc/sphinx/index.html)

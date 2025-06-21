# JSave
JSave is a simple python module for operating on JSON files.

![PyPI - Version](https://img.shields.io/pypi/v/jsave)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jsave)
![PyPI - License](https://img.shields.io/pypi/l/jsave)

## Table of Contents
* [Install](#install)
* [Quick Start](#quick-start)
* [Docs](https://github.com/ethanillingsworth/JSave/wiki)
* [Contributing](#contributing)

## Install
To install JSave use `pip`.
```
pip install jsave
```

## Quick Start

### As a package
To get started with JSave first import functions from `jsave` into your project like this.
```py
from jsave import FUNCTIONS_HERE
```

To find out what to import, and how to use JSave check out the [docs](https://github.com/ethanillingsworth/JSave/wiki).

### As a cmdline utility
To get started with JSave's cmd utility, first find the available modules [here](https://github.com/ethanillingsworth/JSave/wiki/Command-Utility#modules).

Then run a command in your terminal like this:
```
python -m jsave.cmd.MODULE_NAME.COMMAND_NAME
```
## Wiki
For docs and examples for JSave take a look at the [wiki page](https://github.com/ethanillingsworth/JSave/wiki)

## Contributing
All types of contibutions are welcome for the JSave project, whether its updating the documentation, reporting issues, or simply mentioning JSave in your projects.

Remember this before contibuting, you should open an **Issue** if you don't think you can contribute and open a **Pull Request** if you have a patch for an issue.

Sections:
* [Reporting Bugs](#reporting-bugs)
* [Enchancements](#enchancements)
* [Improve Docs](#improve-docs)


### Reporting Bugs
Before you submit a bug report make sure you have the following information or are using the following things.

* Make sure you're on the latest version.
* Make sure its not just on your end (if you were possibly using a python version we dont support).
* Check issues to see if it has already been reported.
* Collect the following info about the bug:
    * Stack Trace.
    * OS, Platform and Version (Windows, Linux, macOS, x86, ARM).
    * Possibly your input and the output.
    * Can you reliably reproduce the issue?

If you have all of that prepared you are more than welcome to open an issue for the community to take a look at.

### Enchancements
If you'd like to enchance something please read this checklist:

* Make sure you're on the latest version.
* Read the [docs](#docs) and find out if what you want to implement is already a feature.
* Search to see if the enhancement has already been suggested (No need to open a new issue if its already there!).
* See if your improvment fits the majority of users, if instead it adds minor functionality consider making a plugin library instead. 
* Describe the enchancement in detail, what does it actually do?

### Improve Docs
If you'd like to improve the [documentation](#docs) please go over the following:

* Read the [docs](#docs) first! If it's already there theres no point adding it.
* Check issues for ideas, issues are a great place to find documentation to add or edit.
* Provide examples for the area youre writing for (eg. showing a code example of how to use the `save` function)

# JSave
JSave is a simple python module for saving data to JSON files.

![PyPI - Version](https://img.shields.io/pypi/v/jsave)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jsave)
![PyPI - License](https://img.shields.io/pypi/l/jsave)

## Table of Contents
* [Install](#install)
* [Quick Start](#quick-start)
* [Docs](#docs)
* [Contributing](#contributing)

## Install
To install JSave use `pip`.
```
pip3 install jsave
```

## Quick Start
To get started with JSave first import functions from `jsave.jsave` into your project like this.
```py
from jsave import FUNCTIONS_HERE
```

To find out what to import, and how to use JSave check out the [docs](#docs).


## Docs

### Save
The save function is used to save `data - dict` to a `filepath - str`.

```py
from jsave import save

data = {
    "This is some dict in python": "It is very cool"
}

# save data as JSON to file save.json
save(data, "save.json")
```


### Read
The read function is used to read data from a `filepath - str`.

```py
from jsave import read

print(read("save.json"))
# {"This is some sample data": "Indeed it is"}
```

If you only want to grab specific keys you can specify them with the `keys - [str]` parameter.

```py
from jsave import read

print(read("save.json", keys=["Hello"]))
# {"Hello": "World"}
```

If one of the keys you're searching for dosent exist then you'll get an error like this.
```
Exception: 'World' could not be loaded, please make sure it is in 'save.json'
(or set parameter 'safe_mode' to False)
```

If you would like to skip over keys the read function cant find set `safe_mode - bool` to `False`.

```py
from jsave import read

print(read("save.json", keys=["Hello", "Guy"], safe_mode=False))
# Cannot find key Guy, but safe_mode is False so it skips over it.
# {"Hello": "World"}
```

### Delete
The read function is used to delete a file provided by `filepath - str`.

```py
from jsave import delete

delete("save.json")
# file is deleted
```

### Merge
THIS FUNCTION IS CURRENTLY NOT IMPLEMENTED!!!!

The merge function is used to combine multiple `files - [str]` and save to a `output_filepath - str`.

```py
from jsave import merge

merge(["save.json", "newsave.json"], "output.json")
# new file named output.json with contents of both save.json and newsave.json.
```

### JSONData
JSONData contains a variety of methods to use on JSON Data, It can be created from a `string` containing JSON Data, from the `read` function or from a python `dict`.

```py
from jsave import JSONData, read

# from string
stringdata = '{"Im some": "Json Data"}'
jdata = JSONData(stringdata)

# from read
jdata = read("save.json")

# from dict
somedata = {
    "Hello": "World"
}

jdata = JSONData(somedata)
```

#### prettify
The prettify method returns the JSONData in a pretty format which `indent - int` size can be specifed.

```py
from jsave import JSONData

# from dict
somedata = {"Hello": "World"}

jdata = JSONData(somedata)

print(jdata.prettify())
#output:
#{
#    "Hello": "World"
#}

print(jdata.prettify(indent=2))
#output:
#{
#  "Hello": "World"
#} 
```

#### set_value
The set_value method works in a similar way to setting keys for dicts with some added comfort featues

Set a single value
```py
from jsave import JSONData

# from dict
somedata = {"Hello": "World"}

jdata = JSONData(somedata)

jdata.set_value("Hello", 10)

print(jdata)
# {"Hello": 10}
```


Set a nested value
```py
from jsave import JSONData

# from dict
somedata = {
    "Hello": {
        "World": 10
    }
}

jdata = JSONData(somedata)

jdata.set_value("Hello/World", 467)

print(jdata)
# {"Hello": {"World": 467}}
```

Set a value that dosent exist
```py
from jsave import JSONData

# from dict
somedata = {}

jdata = JSONData(somedata)

jdata.set_value("Hello/World", 467)

print(jdata)
# {"Hello": {"World": 467}}
```

#### get_value
The get_value method works in a similar way to getting keys from a dict

```py
from jsave import JSONData

# from dict
somedata = {
    "Hello": {
        "World": 10
    }
}

jdata = JSONData(somedata)

print(jdata.get_value("Hello/World"))
# 10
```

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

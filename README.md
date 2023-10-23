# TIME TRACKER
#### Video Demo:  <https://www.youtube.com/>
## Description:
Time Tracker is a useful tool for tracking how many hours you spending in each application during the workday. This will help you to make a recap by the end of your the day.

Application tracking data will be stored in `JSON` format.

### Build with
* [Python 3.11.4](https://www.python.org/downloads/release/python-3114/)

## Table of Contents

- [Getting Started](#getting-started)
    - [Installation](#installation)
- [Usage](#usage)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Mac](#mac)
- [Features](#features)
    - [Interface](#interface)
- [Develop Process](#develop-process)
    - [ctypes library](#ctypes-library)
- [License](#license)
- [Contact](#contact)

## Getting Started

### Installation
> Will be available after uploading to GitHub

## Usage
### Windows
Head to the "root" directory where the `project.py` and open `cmd` there (Command Prompt), then write:
```
project.py
```
If Python is not already in your system's PATH environment variable:
```
python project.py
```
or
>_If you have multiple versions of Python installed on your system_
```
python3 project.py
```

This will start program execution. You can minimize `cmd` window and program will monitor your actions in the background.

To **stop** execution, open `cmd` and press: **`Ctrl+C`**.

And when you finish the program, you will get all your saved data in `user_data\data_apps.json` in JSON format, for example:
```
{
    "Visual Studio Code": {
        "2023-10-22": 29,
        "2023-10-12": 50
    },
    "Google Chrome": {
        "2023-10-22": 4
    },
    "Total Time": {
        "Visual Studio Code": 79,
        "Google Chrome": 4,
    }
}
```
Here we can see how user data represented, for more info, go to the [Features](#features).


### Linux
> Currently unavailable
### Mac
> Currently unavailable

## Features
In addition, program has a feature as **"Command-line arguments"**, and there are several commands to use:
> firstly write `python project.py` and then command.
* today
* list
* total <app_name>
* today <app_name>

:`today` : Returns a list with apps you used today and the time you spent on them.

:`list` : Returns a list of all the apps you have ever used before.

:`total <app_name>` : Returns total time you spent on specific app that you have selected.

:`today <app_name>` : Returns only amount of time you spent today on specific app that you have selected.

> In the next version I will use [argparse](https://docs.python.org/3/library/argparse.html) module to handle "Command-line arguments".

### Interface
> Under development

## Develop Process
```
project/
├── system_getter
│   ├── __init__.py
│   ├── linux_title_getter.py
│   └── windows_title_getter.py
├── user_data
│   └──data_apps.json
├── README.md
├── project.py
├── test_project.py
├── timer.py
└── requirements.txt
```
When the user runs `project.py` in the package `system_getter` we define which system is currently in use via `__init__.py`, it initilizes corresponding file `linux_title_getter.py` or `windows_title_getter.py` with `window_title` function.

>Explanation for Windows
### ctypes library

In this project I used [ctypes](https://docs.python.org/3/library/ctypes.html) foreign function library for Python. It provides **C compatible** data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

I didn't want to use external libraries hence I chose `ctypes`, but if you want there is [pywin32](https://pypi.org/project/pywin32/) which provides access to many of the Windows APIs from Python.

### system_getter/windows_title_getter.py

`ctypes` exports on Windows ***windll*** for loading dynamic link libraries(DLL).
```
from ctypes import windll
```

To create a mutable memory block containing unicode characters of the C type ***wchar_t***, use the `create_unicode_buffer()` function:
```
from ctypes import create_unicode_buffer
```

#### :function : __window_title()__

Using `print(window_title.__doc__)` get docstring:
```
def window_title() -> str or None:
    hwnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buffer = create_unicode_buffer(length)

    windll.user32.GetWindowTextW(hwnd, buffer, length + 1)

    if buffer.value:
        return filter(buffer.value)
    else:
        return filter(None)
```
That function obtains the title of foreground app.

:`var hwnd`: Retrieve a window handle.

:`var length`: The maximum number of characters to copy to the buffer.

:`var buffer`: Create a mutable memory block containing unicode characters(text).

:`method .GetWindowTextW`: Copies the text of the specified window's title bar into a buffer.

#### :function : __filter(window_title)__
>Here I have dealt with one app "Telegram" situation, where I got `hwnd` window handle instead of title bar.

### timer.py

This is the basic counter which I implemented in the class. Here I used `time` module to count 1 second, and `datetime` to get the current date when program is used.

If `window_title()` returns ***None*** the `timer_entry()` stops execution of the main cycle in `project.py` and go on with another attempt to get current window title bar.

### test_project.py

Here I used `pytest` module to implement basic tests for main `project.py` file.

### requirements.txt

Contains a list of all libraries installed using pip that my project requires, one per line.

## License

MIT

## Contact
e-mail: yevhenii.memruk@gmail.com

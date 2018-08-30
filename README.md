# 📸 screenshot: Better macOS Screencaptures via the Terminal

`screenshot` is a command line utility that lets you specify an *application name* and *window title* to take a screenshot of a specific window.

Using `screenshot` you can capture windows belonging to an application, or only an application's windows with certain titles.

## Justification and Use Case
The macOS `screencapture` utility is not developer friendly. 

To programmatically take a screenshot of an application, or a specific window, you must supply a *window ID* to `screencapture`.
In order to find a window's *window ID*, you'll need call out to Quartz.

In newer versions of macOS, the `screencapture` utility improves the user experience slightly: you can run the command and then click on the window you'd like to capture.

However, that necessitates that the user clicks a window each time. You cannot include this as part of an automated pipeline.

To that end, I use this utility to automatically generate screenshots of web, mobile and desktop applications.

## Example
Take a screenshot of the current Terminal window and view it with Preview.app:
```bash
open "`screenshot Terminal`"
```

Take a screenshot of the Pycharm application with the *window title* containing "screenshot":
```bash
screenshot Pycharm -t screenshot
```


## Installation
You will need Python 3.6+. Please install it with `brew` or `ports` if you do not have it already.

### PyPI
```bash
pip3 install screenshot
```

### Github Source
Grab the source, run the following in the source dir:
```bash
pip3 install -r requirements.txt
```

then run
```bash
python3 setup.py install
```

## Usage
`screenshot --help`

```
Usage: screenshot [OPTIONS] APPLICATION_NAME

Options:
  -w, --window_selection_options TEXT
                                  Options: all_windows, on_screen_only,
                                  above_window, below_window, include_window,
                                  exclude_desktop
                                  Default: exclude_desktop
                                  on_screen_only
  -t, --title TEXT                Title of window from APPLICATION_NAME to
                                  capture.
  -f, --filename TEXT             Filename to save the captured PNG as.
  -a, --all_windows               Capture all windows matching parameters.
  -o, --output TEXT               Image format to create, default is png
                                  (other options include pdf, jpg, tiff)
  -s, --shadow                    Capture the shadow of the window.
  --help                          Show this message and exit.
```

## License
See `LICENSE`

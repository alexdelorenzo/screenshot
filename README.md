# 📸 screenshot
## Better macOS Screencaptures via the Terminal

`screenshot` is a command line utility that lets you specify an *application name* and *window title* to take a screenshot of a specific window.

## Justification and Use Case
The macOS `screencapture` utility is not developer friendly. 

To programmatically take a screenshot of an application, or a specific window, you must supply a *window ID* to `screencapture`.
In order to find a window's *window ID*, you'll need call out to Quartz.

In newer versions of macOS, the `screencapture` utility improves the user experience slightly: you can run the command and then click on the window you'd like to screenshot.
However, this necessitates that the user clicks a window each time. You cannot include this as part of an automated pipeline.

To that end, I use this utility to automate the generation of screenshots of web, mobile and desktop applications.

## Example
Take a screenshot of the Pycharm application with the *window title* containing "screenshot".

`screenshot Pycharm -t screenshot`


## Installation
## PyPI
`pip3 install screenshot`

### Github Source
Grab the source, run the following in the source dir:
`pip3 install -r requirements.txt`

then run
`python3 setup.py install`

## Usage
`screenshot --help`

```
Usage: screenshot [OPTIONS] [APPLICATION_NAME]

Options:
  -w, --window_selection_options TEXT
                                  Options: above_window below_window
                                  all_windows include_window on_screen_only
                                  exclude_desktop
                                  Default: exclude_desktop
                                  on_screen_only
  -t, --title TEXT                Title of window from APPLICATION_NAME to
                                  capture.
  -f, --filename TEXT             Filename to save the captured PNG as.
  -a, --all_windows               Capture all windows matching parameters
  --help                          Show this message and exit.
```

## License
See `LICENSE`

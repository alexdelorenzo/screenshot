# pyscreencapture
## Take screenshots on Mac OS X from the command line

pyscreencapture lets you specify an Application Name and Window Title to take a screenshot of a specific window via the commandline.
It's a thin wrapper that grabs the window IDs from Quartz and passes them to `screencapture`.

## Example
Take a screenshot of the Pycharm application with the window title containing "pyscreencapture".

`python3 screencapture.py Pycharm -t pyscreencapture`


## Installation
Grab the source, run the following in the source dir:
`pip3 install -r requirements.txt`

then run
`python3 pyscreencapture.py --help`

## Help
`python3 pyscreencapture.py --help`

```
Usage: screencapture.py [OPTIONS] [APPLICATION_NAME]

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

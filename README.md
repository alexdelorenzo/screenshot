# pyscreencapture
## Take screenshots on Mac OS X from the command line like God intended

pyscreencapture let's you specify an Application Name and Window Title to take a screenshot of a specific window via the commandline.
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
Usage: screencapture.py [OPTIONS] APPLICATION_NAME

Options:
  -t, --title TEXT                Title of window from APPLICATION_NAME to
                                  capture.
  -f, --filename TEXT             Filename to save the captured PNG as.
  -w, --window_selection_options TEXT
                                  Options: above_window on_screen_only
                                  include_window all_windows exclude_desktop
                                  below_window
  --help                          Show this message and exit.
```

## License
See `LICENSE`
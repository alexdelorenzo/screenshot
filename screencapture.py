#!/usr/bin/python3

from itertools import chain
from datetime import datetime
from subprocess import getstatusoutput

import click

from get_window_id import gen_window_ids, options, user_options_str


FILE_EXT = '.png'
COMMAND = 'screencapture -l %s "%s"'
STATUS_OK = 0


class ScreencaptureEx(Exception):
    pass


def take_screenshot(window: int, filename: str, **kwargs) -> str:
    rc, output = getstatusoutput(COMMAND % (window, filename))

    if rc != STATUS_OK:
        raise ScreencaptureEx("Error in screenccapture command '%s'; Return code: %s Output: %s" % (COMMAND, rc, output))

    return filename


def _filename(*args) -> str:
    return '_'.join(map(str, args + (datetime.now(),))) + FILE_EXT


@click.command
@click.option('-w', '--window_selection_options', default=user_options_str,
              help="Options: " + ', '.join(options) + '\nDefault: ' + user_options_str)
@click.option('-t', '--title', default=None, help="Title of window from APPLICATION_NAME to capture.")
@click.option('-f', '--filename', default=None, help="Filename to save the captured PNG as.")
@click.option('-a', '--all_windows', is_flag=True, default=False, help="Capture all windows matching parameters.")
@click.argument('application_name')
def screenshot_window(application_name: str, title: str='', filename: str='', window_selection_options: str='',
                      all_windows: bool=False, **kwargs):
    windows = gen_window_ids(application_name, title, window_selection_options)

    try:
        window = next(windows)

    except StopIteration as ex:
        raise ValueError("Window with parent %s and title %s not found." % (application_name, title)) from ex

    if all_windows:
        windows = chain((window,), windows)

        for window in windows:
            filename = _filename(application_name, title)
            print(take_screenshot(window, filename))

    else:
        filename = filename if filename else _filename(application_name, title)
        print(take_screenshot(window, filename))


if __name__ == "__main__":
    screenshot_window()

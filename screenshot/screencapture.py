#!/usr/bin/python3
from itertools import chain
from datetime import datetime
from subprocess import getstatusoutput
from typing import List, Iterable

import click

from .get_window_id import gen_window_ids, WINDOW_OPTIONS, USER_OPTS_STR

FILE_EXT = '.png'
COMMAND = 'screencapture -l %s "%s"'
STATUS_OK = 0
STATUS_FAIL = 1


class ScreencaptureEx(Exception):
    pass


def take_screenshot(window: int, filename: str, **kwargs) -> str:
    rc, output = getstatusoutput(COMMAND % (window, filename))

    if rc != STATUS_OK:
        raise ScreencaptureEx(f"Error in screenccapture command '{COMMAND}'; Return code: {rc} Output: {output}")

    return filename


def get_filename(*args) -> str:
    return ' '.join(map(str, args + (datetime.now(),))) + FILE_EXT


def gen_windows(application_name: str, title: str, window_selection_options: str) -> Iterable[int]:
    windows = gen_window_ids(application_name, title, window_selection_options)

    try:
        window = next(windows)
        yield window

    except StopIteration as ex:
        raise ScreencaptureEx("Window with parent %s and title %s not found." % (application_name, title)) from ex

    yield from windows


def screenshot_windows(application_name: str, title: str = '', window_selection_options: str = '') -> List[str]:
    filenames: List[str] = []
    windows = gen_windows(application_name, title, window_selection_options)

    for window in windows:
        filename = take_screenshot(window, get_filename(application_name, title))
        filenames.append(filename)

    return filenames


def screenshot_window(application_name: str,
                      title: str = '',
                      filename: str = '',
                      window_selection_options: str = '') -> str:
    windows = gen_windows(application_name, title, window_selection_options)
    window = next(windows)
    filename = filename if filename else get_filename(application_name, title)
    return take_screenshot(window, filename)


@click.command()
@click.option('-w', '--window_selection_options', default=USER_OPTS_STR,
              help="Options: " + ', '.join(WINDOW_OPTIONS) + '\nDefault: ' + USER_OPTS_STR)
@click.option('-t', '--title', default='', help="Title of window from APPLICATION_NAME to capture.")
@click.option('-f', '--filename', default=None, help="Filename to save the captured PNG as.")
@click.option('-a', '--all_windows', is_flag=True, default=False, help="Capture all windows matching parameters.")
@click.argument('application_name')
def run(application_name: str,
        title: str = '',
        filename: str = '',
        window_selection_options: str = '',
        all_windows: bool = False):
    try:
        if all_windows:
            for filename in screenshot_windows(application_name, title, window_selection_options):
                print(filename)

        else:
            print(screenshot_window(application_name, title, filename, window_selection_options))

        exit(STATUS_OK)

    except ScreencaptureEx as e:
        print('Error:', e)
        exit(STATUS_FAIL)


if __name__ == "__main__":
    screenshot_window()

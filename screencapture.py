#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import os
import tempfile
import time
import imagehash as imagehash
from PIL import Image
from itertools import chain
from datetime import datetime
from subprocess import getstatusoutput

import click

from get_window_id import gen_window_ids, options, user_options_str

TOLERANCE = 3
COMMAND = 'screencapture %s -l %s "%s"'
STATUS_OK = 0


class ScreencaptureEx(Exception):
    pass


def take_screenshot(opts: str, window: int, filename: str, **kwargs) -> str:
    command = COMMAND % (' '.join(opts), window, filename)
    rc, output = getstatusoutput(command)

    if rc != STATUS_OK:
        raise ScreencaptureEx("Error in screenccapture command '%s'; Return code: %s Output: %s" % (COMMAND, rc, output))

    return filename


def _filename(file_ext: str, *args) -> str:
    return '_'.join(map(str, args + (datetime.now(),))) + file_ext


@click.command()
@click.option('-w', '--window_selection_options', default=user_options_str,
              help="Options: " + ', '.join(options) + '\nDefault: ' + user_options_str)
@click.option('-t', '--title', default='', help="Title of window from APPLICATION_NAME to capture.")
@click.option('-f', '--filename', default=None, help="Filename to save the captured PNG as.")
@click.option('-a', '--all_windows', is_flag=True, default=False, help="Capture all windows matching parameters.")
@click.option('-t', '--type', default=None,
              help="Image format to create, default is png (other options include pdf, jpg, tiff)")
@click.option('-i', '--interval', default=0, help="Capture interval in seconds. Do not duplicate similar images")
@click.option('-o', '--no_shadow', is_flag=True, default=False, help="Do not capture the shadow of the window.")
@click.argument('application_name')
def screenshot_window(application_name: str,
                      title: str = '',
                      filename: str = '',
                      window_selection_options: str = '',
                      all_windows: bool = False,
                      interval: int = None,
                      no_shadow: bool = False,
                      type: str = 'png',
                      **kwargs):

    opts = []
    file_ext = '.png'

    if no_shadow:
        opts.append("-o")

    if type == 'jpg':
        opts.append("-t jpg")
        file_ext = '.jpg'

    if type == 'tiff':
        opts.append("-t tiff")
        file_ext = '.tiff'

    if type == 'pdf':
        opts.append("-t pdf")
        file_ext = '.pdf'

    windows = gen_window_ids(application_name, title, window_selection_options)

    try:
        window = next(windows)

    except StopIteration as ex:
        raise ScreencaptureEx("Window with parent %s and title %s not found." % (application_name, title)) from ex

    if all_windows:
        windows = chain((window,), windows)

        for window in windows:
            filename = _filename(file_ext, application_name, title)
            print(take_screenshot(opts, window, filename))
        exit()

    if interval > 0:
        prev_hash = ''
        while True:
            base_filename = _filename(file_ext, application_name, title)
            temp_filename = "%s/%s" % (tempfile.gettempdir(), base_filename)

            take_screenshot(opts, window, temp_filename)

            if os.path.isfile(temp_filename):
                image_hash = imagehash.average_hash(Image.open(temp_filename))
                if not prev_hash or abs(prev_hash - image_hash) > TOLERANCE:
                    os.rename(temp_filename, base_filename)
                    print("Captured %s" % base_filename)
                    prev_hash = image_hash
                else:
                    os.remove(temp_filename)

            time.sleep(interval)
        exit()

    filename = filename if filename else _filename(file_ext, application_name, title)
    print(take_screenshot(opts, window, filename))


if __name__ == "__main__":
    screenshot_window()

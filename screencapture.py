from datetime import datetime
from subprocess import getstatusoutput

import click

from get_window_id import gen_window_ids, options, user_options_str


@click.command()
@click.option('-t', '--title', default=None, help="Title of window from APPLICATION_NAME to capture.")
@click.option('-f', '--filename', default=None, help="Filename to save the captured PNG as.")
@click.option('-w', '--window_selection_options', default=user_options_str, help="Options: " + ' '.join(option for option in options))
@click.argument('application_name')
def screenshot_window(application_name: str, title: str=None, filename: str=None, window_selection_options: str=None, **kwargs):
    if not filename:
        filename = '_'.join(map(str, (application_name, title, datetime.now()))) + '.png'

    try:
        window = next(gen_window_ids(application_name, title, window_selection_options))

    except StopIteration as ex:
        raise ValueError("Window with parent %s and title %s not found." % (application_name, title)) from ex

    rc, output = getstatusoutput('screencapture -l %s "%s"' % (window, filename))

    if rc == 0:
        print(filename)

        return filename

    else:
        raise Exception("Error in screencapture command %s: %s", (rc, output))


if __name__ == "__main__":
    screenshot_window()
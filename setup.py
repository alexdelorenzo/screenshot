import os
from os import getcwd

from setuptools import setup
from pathlib import Path

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as file:
    readme = file.read()


requirements = [line
                for line in Path('requirements.txt').read_text().split('\n')
                if line]

CMD = 'screenshot'

# OPTIONS = {
#     'argv_emulation': True,
#     'plist': {
#         'LSUIElement': True,
#     },
#     'packages': ['objc', 'cv2', 'face_recognition'],
#     'bdist_base': str(Path(getcwd()).parent) + '/build',
#     'dist_dir': str(Path(getcwd()).parent) + '/dist'
# }

setup(
    name="screenshot",
    version="1.0.0",
    author="Alex DeLorenzo",
    author_email="alexdelorenzo@gmail.com",
    description="Take screenshots on macOS",
    license="AGPL-3.0",
    keywords="screenshot macos osx apple screencapture pyscreencapture",
    url="https://github.com/thismachinechills/pyscreencapture",
    packages=['screenshot'],
    long_description=readme,
    zip_safe=True,
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'console_scripts':
            [f'{CMD} = screenshot.screencapture:run']
    },
    #
    # ## app nonsense
    # app=['brightness/change_brightness.py'],
    # datafiles=['brightness/.'],
    # WINDOW_OPTIONS={'py2app': OPTIONS},
    # setup_requires=['py2app']

)

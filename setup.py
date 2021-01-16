import os
from os import getcwd

from setuptools import setup
from pathlib import Path


readme = Path("README.md").read_text()

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
            [f'{CMD} = screenshot.mac.capture:run']
    },
    #
    # ## app nonsense
    # app=['brightness/change_brightness.py'],
    # datafiles=['brightness/.'],
    # WINDOW_OPTIONS={'py2app': OPTIONS},
    # setup_requires=['py2app']

)

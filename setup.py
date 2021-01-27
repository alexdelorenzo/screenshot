import os
from os import getcwd

from setuptools import setup
from pathlib import Path


readme = Path("README.md").read_text()

requirements = [line
                for line in Path('requirements.txt').read_text().split('\n')
                if line]

CMD = 'screenshot'


setup(
    name="screenshot",
    version="1.0.2",
    author="Alex DeLorenzo",
    author_email="alexdelorenzo@gmail.com",
    description="Take screenshots on macOS",
    long_description_content_type="text/markdown",
    license="AGPL-3.0",
    keywords="screenshot macos osx apple screencapture pyscreencapture",
    url="https://github.com/alexdelorenzo/screenshot",
    packages=['screenshot'],
    long_description=readme,
    zip_safe=True,
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'console_scripts':
            [f'{CMD} = screenshot.mac.capture:run']
    },
)

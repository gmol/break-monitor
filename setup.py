from setuptools import setup
import re


with open('README.md') as fp:
    long_description = fp.read()


def find_version():
    with open('states/__init__.py') as fp:
        for line in fp:
            # __version__ = '0.1.0'
            match = re.search(r"__version__\s*=\s*'([^']+)'", line)
            if match:
                return match.group(1)
    assert False, 'cannot find version'


setup(
    name='breakalert',
    version=find_version(),
    packages=['states'],
    description='Raspberry Pi Zero project to remind about break time',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    maintainer='Gmol',
    maintainer_email='arthur.gmol@gmail.com',
    url='https://github.com/gmol/breakalert.git',
)

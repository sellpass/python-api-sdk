from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Python SDK for Sellpass.'
LONG_DESCRIPTION = 'A package that allows for easier usage of the Sellpass Api.'

setup(
    name="sellpass",
    version=VERSION,
    author="Sellpass",
    author_email="<team@sellpass.io>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['httpx'],
    keywords=['sellpass', 'sdk', ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)

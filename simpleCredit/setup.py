import os
import sys
from distutils.core import setup

sys.path.append('simpleCredit')

setup(
    name = "SimpleCreditCardProcesssing",
    version = "0.0.1",
    author = "Chenyang Liu",
    author_email = "neoliu0831@gmail.com",
    description = ("A test program for Braintree "),
    license = "Unknown",
    keywords = "N/A",
    url = "N/A",
    packages=['simpleCredit', 'test'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: None",
    ],
)

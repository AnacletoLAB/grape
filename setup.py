import os
import re

# To use a consistent encoding
from codecs import open as copen
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with copen(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def read(*parts):
    with copen(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


__version__ = find_version("grape", "__version__.py")

test_deps = []

# TODO: Authors add your emails!!!
authors = {
    "Luca Cappelletti": "luca.cappelletti1@unimi.it",
    "Tommaso Fontana": "tommaso.fontana@mail.polimi.it",
    "Vida Ravanmehr": "vida.ravanmehr@jax.org",
    "Peter Robinson": "peter.robinson@jax.org",
}


setup(
    name='grape',
    version=__version__,
    description="Rust/Python for high performance Graph Processing and Embedding.",
    long_description=long_description,
    url="https://github.com/LucaCappelletti94/dict_hash",
    author=", ".join(list(authors.keys())),
    author_email=", ".join(list(authors.values())),
    # Choose your license
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    tests_require=test_deps,
    install_requires=[
        "ensmallen>=0.6.1",
        "embiggen>=0.9.0",
    ]
)

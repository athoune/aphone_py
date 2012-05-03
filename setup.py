#!/usr/bin/env python

from setuptools import setup

# http://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(name='aphone',
    version='0.0.1',
    package_dir={'': 'src'},
    url='http://github.com/athoune/aphone_py',
    #scripts=[],
    description="Building python code to apply phonetic rules.",
    long_description="""
Python implementation for aphone.
""",
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Natural Language :: French',
          'Topic :: Text Processing :: Linguistic',
          'Topic :: Text Processing :: Filters',
        ],
    license="LGPL",
    author="Mathieu Lecarme",
    packages=['aphone_py'],
    keywords=["phonetic", "aspell"],
    scripts=['bin/aphone-py'],
    zip_safe=True,
    install_requires=[],
)


#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='learning',
      version='0.0.4',
      description='Getting Started with Python unit testings, documentations, CI and code coverage',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='Andrew Huy Nguyen',
      author_email='andrewhuynguyen10@gmail.com',
      url='https://github.com/andrewhuynguyen/getting-started',
      setup_requires=['pytest-runner',],
      tests_require=['pytest','python-coveralls'],
      install_requires=[
          "numpy",
      ],
      packages=['learning'],
      scripts=[],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Windows',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
     )

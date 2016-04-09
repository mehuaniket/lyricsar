#!/usr/bin/env python
from distutils.core import setup

setup(
    name='lyricsar',
    version='0.5.0',
    description='lyrics fetcher from website',
    long_description='''lyricsar is a tool for extracting lyrics from website.
                        Unlike other tools, it focuses entirely on getting
                        and fetching lyrics from website. lyricsar allows to
                        obtain the exact lyrics from page.
                        It includes a converter that can transform lyrics
                        into other text formats (such as HTML).''',
    license='MIT',
    author='Aniket patel',
    author_email='ceaniket@gmail.com',
    url='http://github.com/ceaniket/lyricsar',
    packages=['lyricsar'],
    scripts=[
    'lyrics.py'
    ],
    keywords=['fetch lyrics','lyrics analysis', 'lyrics mining'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Topic :: lyrics fetcher',
    ],
    )

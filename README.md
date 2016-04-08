# lyricsar version 0.4.0-alpha
with fast performance
> " A Man Can Do as he Will, but not Will as he Will " :)

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration
 * Contribution
 * contact

Introduction
----------------
  - project have very simple purpose that fetches lyrics from the the specific website( means if plugin_method is available for website)
  - you can add your plugin for any website, but you need to understand structure of plugin .
  - I also want add player on terminal library which can play song in current dir in and pass the title of mp3 directly to script that fetches lyrics for song!!
  - I think this project is for programmer's only if you are not, it's pathetic to use! :)

Requirements
----------------
  - first'n first you need python 2.7 :)
  - you need to install BeautifulSoup library if not come with default installation.

 ```
 $ apt-get install python-bs4
or
 $ easy_install beautifulsoup4
or
 $ pip install beautifulsoup4

 ```

  - it's great and make easy if you use ubuntu or other linux dist!
  - if you get an error on if other neccessary library not available, you need to install as above!

Installation
----------------

  - to install project in your computer download project zip and run setup script.

 ```
 $ python setup.py install

 ```

  - project automatically install script that run from anywhere like following!

 ```
 $ lyrics.py "title of the song"

 ```

  - I also describe all decisions and ideas about project in ideastruct.md file,ove to write this type of file.

Configuration
-----------------
  - you can configure the project with file name setting.py .
  - you can remove name of module that also remove support for that website.

Contribution
----------------
- always feel free to help out !whether if's filing bugs and feature request.
- for now, you can add more plugin kind methods to project that is one of the important thing.



Contact
-----------
> mail me: ceaniket@gmail.com
> [fork me on github](https://github.com/ceaniket/lyricsar)

#lyricsar version 0.3.0

###CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Contribution
 * Configuration
 * contact

###Introduction
----------------
  - project have very simple purpose that fetches lyrics from the the specific website( means if plugin is available for website)
  - you can add your plugin for any website, but you need to understand structure of plugin .
  - i also want add player on terminal library which can play song in current dir in and pass the title of mp3 directly to script that fetches lyrics for song!!
  - i think this project is for developer's only because it's pathetic to use! :)

###Requirements
----------------
  - you need to install BeautifulSoup library.

 ```
 $ apt-get install python-bs4
or
 $ easy_install beautifulsoup4
or
 $ pip install beautifulsoup4

 ```

  - it's great or been easy if you use ubuntu or other linux flavour!

###Installation
----------------

   - to install project in your computer download project zip and run setup script.

 ```
 $ python setup.py install

 ```

   - project automatically install script that run from anywhere!like following!

 ```
 $ lyrics.py [title of the song]

 ```


   - i also describe all decision and ideas about project in ideastruct.md file.i love to write this type of file.

###Contribution
----------------
- always feel free to help out !whether if's filing bugs and feature request.
- for now, you can add more plugin to project that is one of the important thing.
- for understand the plugin structure refer the README.md in plugin folder.
- you also understand the structure with just seeing commit because when  you see commit or diff tool you can get commentary of changes that changes in ideastruct.md on every commit.

###Configuration
-----------------
- you can configure the project with file name config.py .
- you can remove name of module that also remove support for that website.

###Contact
-----------
mail me: ceaniket@gmail.com

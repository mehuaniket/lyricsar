#lyricsar version 0.1.0

##CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Contribution
 * Configuration
 * contact

###Introduction
----------------
  - project have very simple purpose that fetches lyrics from the the specific website(it's means if plugin is available for website)
  - you can add your plugin for any website, but you need to understand structure of plugin .
  - i also add player on terminal library which can play song for current dir in and pass the title of mp3 directly(future).
  - this version is for developer's only because it's pathetic to use! :)

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

   -it's easy run script from terminal name lyricsar.

       ```
       $python lyricsar.py

       ```

   -and for this version you also need to give name in commandline.!!

       ```python

       $python lyricsar.py [title of the song]

       ```

   -it's bit complicate FOR ME  but i'm working on making command that simply run from anywhere

   -i also describe all decision and ideas about project in ideastruct.md file.

   -i love to write this type of file.

###Contribution
----------------
-always feel free to help out !whether if's filing bugs and feature request.
-for now, you can add more plugin to project that is one of the important thing.
-for understand the plugin structure refer the README.md in plugin folder.
-you also understand the structure with just seeing commit because when you see commit or diff tool you can get commentary of changes from changes in ideastruct.md on every commit.

###Configuration
-----------------
-you can configure module that you want to be used in main module by configuring plugin.conf file .
-you can remove name module that also remove support for that website.

###contact
-----------
mail me: ceaniket@gmail.com

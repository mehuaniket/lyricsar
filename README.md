#lyricsar version 0.1.0

###CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Configuration

####Introduction
----------------
  - project have very simple purpose that fetches lyrics from the the specific
    website
  - you can add your plugin for any website but you need to understand structure
    of plugin .
  - i also add player on terminal library which can play song for current dir in
    and pass the title of mp3 directly.
  - this version is for developer's only because it's not easy to use! :)

####Requirements
----------------
  - you need to install BeautifulSoup library.

       ```
       $ apt-get install python-bs4
       or
       $ easy_install beautifulsoup4
       or
       $ pip install beautifulsoup4
       ```

  - it's great if you use ubuntu or other linux flavour!

####Installation
----------------

   -it's easy run script from terminal name lyricsar.

       ```
       $python lyricsar.py
       ```

   -and for this version you also need to specify name or path of mp3.!!(sorry)

       ```python
       tag = tinytag.TinyTag.get('music\Bin Tere (Reprise) .mp3',image=True)
       ```

   -it's bit complicate but i'm working on making command that simply run from
     anywhere

   -i also describe project structure in ideastruct.md file

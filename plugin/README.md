#understand plugin concept:
-i try to make plugin mechanism here but is not mature as other big software   has because i read nothing about that type of mechanism but i want to create that myself by thinking .
-first i would like to draw diagram that give you understanding about plugin.
-name in [box] plugin name .

```
     -------------
     |           |
     |pluginclass|------------------> __init__(title)
     -------------              ->this method is only initialize search
        | |  |  |                 url and title of the song.
        | |  |  |               ->__init__ takes title as argument
        | |  |  |
        | |  |  |-------------------> get_search()
        | |  |                  ->function make url by concate the
        | |  |                    title and URL.
        | |  |                  ->apply yourself and make function return
        | |  |                    url that have search results of title.
        | |  |
        | |  |----------------------> get_link(searchpage)
        | |                     -> take a downloaded page as argument
        | |                     ->this page is search link that have url of
        | |                       page that have lyrics that will return.
        | |
        | |-------------------------> get_lyrics(lyricspage)
        |                       ->take a downloaded page as argument.
        |                       ->page that have div class that havelyrics
        |                         that lyrics is return by this function.
        |
        |---------------------------> __main__
                                ->you can use main as testing.

```

-diagram make clear piture in mind about concept of plugin.
-function of any new plugin have same name that as above.

[+]first I tell you best idea to understand this project, switch to the second
   commit and after read this file. give you best idea what the hell happening
   here.{happy traversing :)}
[+]after primary offline success now, I try to structure whole idea
   and find possible class that easy to maintain and add module that find lyrics
   from multiple website.
[+]first I check success of results online and check that program  is success
   give effective result or what?!
[+]I add [plugin] folder that is for python modules that have basic structure
    about what they do in other word basic definition
    following is basic functions of that module.

    -do_search :
        what they provide is basic url of the page that have lyrics of mp3.
    -get_lyrics:
        get lyrics is provide lyrics of the from link that provide by do_search.

[+]it means first job is to make lyricsmint module that work with above basic
   functions.
[+]what type attributes is received by lyricsmint?
   -all metadata about song only.
[+]at this point in time,how the the plugin files work[basic definition]
   any file in plugin basically four function mention following:
  =>__init__
  =>get_search
  =>get_link
  =>get_lyrics
   all output return string value.
  -__init__:in this initialize class with search url and also provide mp3
    metadata that useful to build search url.

  -get_search:basically this function is return url that fetches the  suggestion
   result from the website.

  -get_link:function provide link from suggestion result and pass it for next
   operation

  -get_lyrics:this function provide lyrics by traversing the page data provide
   by link that return from the get_link() function


[+]now i need to complete pagegetter class that basically necessary for download
   any page from website by given url

[+]my best try is is design modules that are undependable from each Other
   as my view that is great thing for structural design.

[+]next question is what are the function in the pagegetter.py ??

[+]for now,i think that is only one pretty function that necessary.

[+]function take url as argument and provide html data on the request.

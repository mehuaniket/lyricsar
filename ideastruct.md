[+]first I tell you best idea to understand this project, switch to the second commit and after read this file. give you best idea what the hell happening
   here.{happy traversing :)}

[+]after primary offline success now, I try to structure whole idea and find possible class that easy to maintain and add module that find lyrics
   from multiple website.

[+]first I check success of results online and check that module is success give effective result or what?!

[+]I add [plugin] folder that is for python modules that have basic structure about what they do in other word basic definition following is basic functions          of that module.

    -do_search :
        what they provide is basic url of the page that have lyrics of mp3.
    -get_lyrics:
        get lyrics is provide lyrics of the from link that provide by do_search.

[+]it means first job is to make lyricsmint module that work with above basic  functions.

[+]what type attributes is received by lyricsmint?
   -all metadata about song only.
   -and title text only

[+]at this point in time,how the the plugin files work[basic definition]   any file in plugin basically four function mention following:
  =>__init__
  =>get_search
  =>get_link
  =>get_lyrics
   all output return string value.
  -__init__:in this initialize class with search url and also provide mp3  metadata that useful to build search url.

  -get_search:basically this function is return url that fetches the  suggestion
   result from the website.

  -get_link:function provide link from suggestion result and pass it for next
   operation

  -get_lyrics:this function provide lyrics by traversing the page data provide
   by link that return from the get_link() function


[+]now i need to complete pagegetter class that basically necessary for download any page from website by given url

[+]my best try is is design modules that are undependable from each Other as my view that is great thing for structural design.

[+]next question is what are the function in the pagegetter.py ??

[+]for now,i think that is only one pretty function that necessary.

[+]function take url as argument and provide html data on the request.

[+]now time to add class that process string in way we want!

[+]now ,now i only add makeHTML function that process the html_doc and give pure
string.

[+]i also add processTITLE function that process the title of string and make it simple that can increase chance of effective result.

[+]implement main module name lyricsar.py properly.

[+]now try to solve problem with pagegetter class that seems not working!

[+]delete checkout branch and create new branch for name (cmd)

[+]branch cmd target is redefined the communication beetween modules that is better for easy to understand structure of the project and also it's
   help the new user ,he need only understand the working of plugin that give him/her full idea about and starting to write plugin for project.

[+]that is big challenge but not impossible,first challenge is to defined all what they receive and what they have to return.

[+]also i need to add small intelligence that properly find what is title of the song and remove other words or URL from the title.

[+]first i try to remove dependency of tinytag library from lyricsar and is work on commandline argument.

[+]now i think i should remove tinytag dependency from project because it causes
problem when we get title from a song and some time things going complicated.

[+]i remove all tinytag dependency or tag dictionary .

[+]when we want add that feature is simply we do with add extra module .

[+] and removing that whole idea of tinytag now i can concentrate on commandline feature and add new type of plugin.

[+]first i need to handle all possible error in pagegetter class error should come out in informative way.

[+]but first i should merge the cmd repo with master becuase i change whole idea of project for moment.

[+]i tag it "0.2.0-alpha"


[+]i add test folder that really help you when you want  testing lyricsmint.py with out the INTERNET(removed)

[+]basic dynamic plugin loading is working, now trying make syntactically correct  that remove errors.

[+]i will make plugin of google that search lyrics with title and other query user want ,find link from that searchpage and find lyrics.inshort first two function is moved to the google module.

[+]that give us speed to making module for other  website .

[+]now i try to make google search plugin that search with a title that user pass on command line and i use google topical search api that make it very easy
  to get links of search result.topical search api is give us way to get results form small set of website.

[+]for one more time restructuring project because module increases because i make module per class now i try to reorganize class in single module.

[+]rebase mashup the project but i install package in my own computer that all important files backup from there 

[+] first feature added to project ,now we handle error with errorlist module that give proper description of error with error no.
[+]now target is modify google plugin and make that working properly.

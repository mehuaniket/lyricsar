import string
class strprocess:
    """add all extra processing method """
    def __init__(self):
        self.data=""
        self.tags=["</p>","</br>","<br>","<p>","</P>"]
        self.marks=["/","?","-","!","@","#","$","%","^","*","(",")",";","{","}","~"]
    def makehtml(self,data):
        self.data="<"+"html"+">"
        self.data=self.data+data
        self.data=self.data+"<"+"/html"+">"

    def removeHTML(self,page):
        self.page=page
        for tag in self.tags:
            self.page=string.replace(self.page,tag," ")

        return self.page

    def removemarks(self,title):
        self.title=title
        for mark in self.marks:
            self.title=string.replace(self.title,mark,"")

        return self.title



if __name__ =="__main__":
    pro=strprocess()
    print pro.removeHTML("<p>aniket<br>mukeshbhai</br>patel</P>")
    print pro.removemarks("Meherbaan - Bang Bang - WapKing.Cc")

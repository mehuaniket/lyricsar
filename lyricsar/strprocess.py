import string
class strprocess:
    """add all extra processing method """
    def __init__(self):
        self.data=""
        self.tags=["</p>","</br>","<br/>","<br>","<p>","</P>","<div>","</div>"]
        self.marks=["/","?","-","!","@","#","$","%","^","*","(",")",";","{","}","~"]
    def makehtml(self,data):
        self.data="<"+"html"+">"
        self.data=self.data+data
        self.data=self.data+"<"+"/html"+">"

    def addplus(self,title):
        self.title=string.replace(title,"-","+")
        return self.title

    def removeHTML(self,page):
        self.page=page
        for tag in self.tags:
            if tag=="<br/>":
                rep="\n"
                self.page=string.replace(self.page,tag,rep)
            else:
                rep=""
                self.page=string.replace(self.page,tag,"\n")
        return self.page

    def removesign(self,page):
        self.page=page
        self.page=string.replace(self.page,"[","")
        return self.page

    def removemarks(self,title):
        self.title=title
        for mark in self.marks:
            self.title=string.replace(self.title,mark,"")

        return self.title



if __name__ =="__main__":
    pro=strprocess()
    print pro.removeHTML("<p>aniket<br/>mukeshbhai</br>patel</P>")
    print pro.removemarks("Meherbaan - Bang Bang - WapKing.Cc")

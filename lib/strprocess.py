import string
class process:
    """add all extra processing method """
    def __init__(self):
        self.data=""
        self.tags=["</p>","</br>","<br>","<p>","</P>"]

    def makehtml(self,data):
        self.data="<"+"html"+">"
        self.data=self.data+data
        self.data=self.data+"<"+"/html"+">"

    def removeHTML(self,page):
        self.page=page
        for tag in self.tags:
            self.page=string.replace(self.page,tag," ")
            
        return self.page



if __name__ =="__main__":
    pro=process()
    print pro.removeHTML("<p>aniket<br>mukeshbhai</br>patel</P>")

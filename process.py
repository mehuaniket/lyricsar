class process:
    """add all extra processing method """
    def __init__(self):
        self.data=""

    def makehtml(self,data):
        self.data="<"+"html"+">"
        self.data=self.data+data
        self.data=self.data+"<"+"/html"+">"

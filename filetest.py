class filetest:
    """=>this provide content of specific html page to the pagedown class
    =>it easy our working with testing"""
    def __init__(self): # Set name when constructed

        self.f = open("test\MERI AASHIQUI LYRICS - Aashiqui 2.html",'r')
        self.page=""
        try:
            for line in self.f:
                self.page=self.page+line
        finally:
            self.f.close()

    def read(self):

        print "i'm here"
        return self.page

if __name__ == "__main__":
    file_test=filetest()
    print file_test.read()

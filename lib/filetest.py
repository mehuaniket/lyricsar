class filetest:
    """this provide content of specific html page to the  class that need it
    it easy our working with testing"""
    def __init__(self,title):
        self.title=title
        self.f = open(self.title,'r')
        self.page=""
        try:
            for line in self.f:
                self.page=self.page+line
        finally:
            self.f.close()

    def read(self):
        return self.page

if __name__ == "__main__":
    file_test=filetest("test\Search results for tum hi ho.html")
    print (file_test.read())
    filet_test=filetest("test\MERI AASHIQUI LYRICS - Aashiqui 2.html")
    print (file_test.read())

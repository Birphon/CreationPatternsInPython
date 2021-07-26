"""
REPLACE THIS LINE WITH YOUR NAME

TASK:   (1) redesign this system so it uses the BUILDERGOF pattern
        (2) add the additional option mentioned at the end
"""
class HTMLDoc(object):
    def __init__(self):
        self.tokens = []
    def parse(self, text, type):
        """This design is inflexible.
            The case statement in this method
            will forever have to be edited and extended
        """
        if type == 'HEAD':
            self.tokens.append( "<H1>" + text + "</H1>" )
        elif type == 'FONT':
            self.tokens.append( "<FONT>" + text + "</FONT>" )
        elif type == 'PARA':
            self.tokens.append( "<P>" + text + "</P"  )

class AbstractBuilder(object):
    def __init__(self):
        self.tokens = []
    def getResult(self):
        return self.tokens
    def addHead(self, text): pass
    def addFont(self, text): pass
    def addPara(self, text): pass

            
class HTMLBuilder(AbstractBuilder):
    def addHead(self, text):
        self.tokens.append( "<H1>" + text + "</H1>" )
    def addFont(self, text):
            self.tokens.append( "<FONT>" + text + "</FONT>" )
    def addPara(self, text):
            self.tokens.append( "<P>" + text + "</P"  )


class JSONBuilder(AbstractBuilder):
    def addHead(self, text):
        self.tokens.append( '"H1"="' + text + '"'  )
    def addFont(self, text):
            self.tokens.append( '"FONT"="' + text + '"' )
    def addPara(self, text):
            self.tokens.append( '"P="' + text  + '"' )
    

class TestWriter(object):
    def __init__(self, builder):
        self.builder = builder
    def assess(self):
        self.builder.addFont("timesRoman")
        self.builder.addHead("Once upon a time...")
        self.builder.addPara("There was a student doing a programming test.")
        self.builder.addPara("It was hard")
        return( self.builder.getResult() )        

if __name__ == "__main__":
    print( TestWriter( JSONBuilder() ).assess() )
    # ['<FONT>timesRoman</FONT>', '<H1>Once upon a time...</H1>', '<P>There was a student doing a programming test.</P', '<P>It was hard</P']

"""
additional functionality required is
same input but JSON format output
['"FONT"="timesRoman"', '"H1"="Once upon a time"', '"P"="There was a student doing a programming test.", '"P"="It was hard"']
""" 
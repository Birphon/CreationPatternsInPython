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


if __name__ == "__main__":
    doc = HTMLDoc()
    doc.parse("timesRoman", "FONT" )
    doc.parse("Once upon a time...", "HEAD" )
    doc.parse("There was a student doing a programming test.", "PARA" )
    doc.parse("It was hard", "PARA" )
    print(doc.tokens)
    # ['<FONT>timesRoman</FONT>', '<H1>Once upon a time...</H1>', '<P>There was a student doing a programming test.</P', '<P>It was hard</P']

"""
additional functionality required is
same input but JSON format output
['"FONT"="timesRoman"', '"H1"="Once upon a time"', '"P"="There was a student doing a programming test.", '"P"="It was hard"']
""" 
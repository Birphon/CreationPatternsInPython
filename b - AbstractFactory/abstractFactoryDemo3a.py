"""
Purpose.  Abstract Factory 

Discussion.
Trying to maintain portability across multiple "platforms"
routinely requires lots of preprocessor "case" stmts.
The Factory pattern suggests defining
a creation services interface in a Factory base class,
and implementing each "platform" in a separate Factory derived class.

NEEDS FIXING
"""


class Widget(object):
    def draw(self):
        pass
    
class MotifBtn(Widget):
    def draw(self):
        print("MotifBtn")

class WindowsBtn(Widget):
    def draw(self):
        print("WindowsBtn")


# client methods which contain duplicate code
def doThisWindow():
    # create window, attach btn       
    if MOTIF:
        w = MotifBtn()
    else: # WINDOWS
        w = WindowsBtn()
    #then draw it all
    w.draw()

def doThatWindow():
    # create window, attach btn       
    if MOTIF:
        w = MotifBtn()
    else: # WINDOWS
        w = WindowsBtn()
    #then draw
    w.draw()

#CLIENT code
if __name__ == "__main__":
    MOTIF = True
    # create window, attach btn       
    if MOTIF:
        w = MotifBtn()
    else: # WINDOWS
        w = WindowsBtn()
    # then draw
    w.draw()
    #then call some differing functions
    doThisWindow();           
    doThatWindow();           


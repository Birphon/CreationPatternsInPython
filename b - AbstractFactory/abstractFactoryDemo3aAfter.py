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

class Factory(object):
    def createBtn(self):
        pass
class MotifFactory(Factory):
    def createBtn(self):
        return MotifBtn()
class WindowsFactory(Factory):
    def createBtn(self):
        return WindowsBtn()    
    
# client methods which contain duplicate code
def doThisWindow(factory):
    # create window, attach btn       
    w = factory.createBtn()
    #then draw it all
    w.draw()

def doThatWindow(factory):
    # create window, attach btn       
    w = factory.createBtn()
    #then draw
    w.draw()

#CLIENT code
if __name__ == "__main__":
    MOTIF = False
    # create window, attach btn       
    if MOTIF:
        f = MotifFactory()
    else: # WINDOWS
        f = WindowsFactory()
    # then draw
    w = f.createBtn()
    w.draw()
    #then call some differing functions
    doThisWindow(f);           
    doThatWindow(f);           


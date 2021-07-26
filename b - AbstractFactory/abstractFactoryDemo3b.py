"""
Purpose.  Abstract Factory 

Discussion.
Trying to maintain portability across multiple "platforms"
routinely requires lots of preprocessor "case" stmts.
The Factory pattern suggests
defining a creation services interface in a Factory base class,
and implementing each "platform" in a separate Factory derived class.
MODEL ANSWER
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


class AbstractFactory(object):
    def createBtn(self):
        pass
# concrete factories
class MotifFactory(AbstractFactory):
    def createBtn(self):
        return MotifBtn()
class WindowsFactory(AbstractFactory):
    def createBtn(self):
        return WindowsBtn()

factory = AbstractFactory()
def doThisWindow():
    w = factory.createBtn()
    w.draw()
def doThatWindow():
    w = factory.createBtn()
    w.draw()
    

if __name__ == "__main__":
    MOTIF = True
    if MOTIF:
        factory = MotifFactory()
    else: # WINDOWS
        factory = WindowsFactory()
    # create window, attach btn
    w = factory.createBtn()
    w.draw()
    doThisWindow();
    doThatWindow();
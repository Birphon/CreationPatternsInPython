'''
REPLACE THIS LINE WITH YOUR NAME

rewrite the code below so it uses the builder pattern
with one Director, one abstract Builder class and two concrete Builder subclasses
'''

# PRODUCT CLASSES - leave them alone
class Stuff(object):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)
  
    
class File(Stuff):
    pass

class Queue(Stuff):
    pass

class Password(Stuff):
    pass




    
allData = [ [File, "state.dat"],[File,"config.sys"], [Queue, "compute"], [Queue, "log"], [Password, "abcd"], [File, "homework.doc"] ]

# this client is too busy
# it should just have to decide if it is at home or work and pick the appropriate builder
# and a director should be used to offload much of the worklload too
def client():
    storage = []
    for data in allData:
        #print(data)
        what = data[0]
        where = data[1]
        if SYSTEM == 'home':
            if what == File:
                where = 'c:\\' + where
            elif what == Queue:
                where = 'LOFO: ' + where
            elif what == Password:
                pass
        elif SYSTEM == "work":
            if what == File:
                where = 'h:\\' + where
            elif what == Queue:
                where = 'FOFO: ' + where
            elif what == Password:
                where = where * 3
        thing = what( where )
        storage.append(thing)
    print('\n')
    for thing in storage:
        print(thing)

SYSTEM = 'home'
client()
'''

c:\state.dat
c:\config.sys
LOFO: compute
LOFO: log
abcd
c:\homework.doc
'''

SYSTEM = 'work'
client()
'''

h:\state.dat
h:\config.sys
FOFO: compute
FOFO: log
abcdabcdabcd
h:\homework.doc
'''

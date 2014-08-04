import pdb
import decimal

class Programs:

    def __init__(self, bufferlistp=[8, 3, 4], transitlistm=[1, 2, 3], bufferlist=[]):  # class constructur (called at creation time)
        self.name = ""   # the default name is the empty string
        self.bufferlistp=bufferlistp
        self.transitlistm=transitlistm
        self.bufferlist=bufferlist
        
    def ask(self):
        while 1: # infinite loop
            name = raw_input("Name: ")
            if name == "":
                print "Ops! Retry"
            else:
                print "Hello ", name
                break  # this will break the loop

        self.name = name  # assign to self.name the value name

    def test(self):
        for b, t in zip(self.bufferlistp, self.transitlistm):
            percentage=b*t
            self.bufferlist.append(percentage)

if __name__ == '__main__':
    prog = Programs()
    #pdb.set_trace()
    prog.test()
    print prog.bufferlist

#a=05
#b=30

#schedule[:] = [datetime.strftime(x, '%I:%M%p') for x in schedule]


#dt = datetime.combine(date.today(), time(a, b)) + timedelta(minutes=10)
#print dt.time()
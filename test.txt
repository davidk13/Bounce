class Programs:

    def __init__(self):  # class constructur (called at creation time)
        self.name = ""   # the default name is the empty string

    def ask(self):
        while 1: # infinite loop
            name = raw_input("Name: ")
            if name == "":
                print "Ops! Retry"
            else:
                print "Hello ", name
                break  # this will break the loop

        self.name = name  # assign to self.name the value name


if __name__ == '__main__':
    prog = Programs()
    prog.ask()
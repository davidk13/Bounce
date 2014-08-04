#finished python code
#next I'll work on turning this into a webapp

import datetime

class Bounce:
    """The Never-be-late prototype"""
  
    def __init__(self, schedule, transitlist=[], transitlistm=[], bufferlist=[], 
                 bufferlistp=[], preplist=[], resultlist=[]):
        self.schedule=schedule #starts with a daily schedule
        self.transitlist=transitlist #default empty list of transit methods
        self.transitlistm=transitlistm #default empty list of transit time (in minutes)
        self.bufferlist=bufferlist #default empty list of buffer time in minutes
        self.bufferlistp=bufferlistp #default empty list of buffer time in percentage
        self.preplist=preplist #default empty list of prep time in minutes
        self.resultlist=resultlist #sets up resultlist as an attribute
                
    def time(self): #converts your schedule into a datetime.datetime object
        schedule=self.schedule #am I wrong in thinking that I needed to define this local 
                               #variable for a list comprehension?
        schedule[:] = [datetime.datetime.strptime(x, '%I:%M%p') for x in schedule] 
                    #converts function to datetime object
        self.schedule=schedule #records datetime objects as the new class attribute
    
    def transit(self): #method for accounting for transit time
        for i in self.schedule: #forloop for getting transit method for each appointment
        	transits=0 #default value so that the forloop is started 
        	while transits!='d' and transits!='w': #while clause ensures rawinput is repeated if a mistake is typed in
        	    try:
        	        text=""""How will you be getting to your {0} appointment? Type d for drive and w for walk: """.format(i) #often in my rawinputs, I will refer to an appointment by its time in the schedule via the .format() command. 
        	        transits=raw_input(text) #is there a way to break this up without it showing in the console?
        	        if not (transits=='d' or transits=='w'): #if not d or w, an exception is raised
        	            raise ValueError 
        	    except ValueError: 
        	        print "Invalid transit method. Please type d or w" #message on error telling the user to type d or w 
        	    else:
        	        self.transitlist.append(transits) #if a correct input is typed, records the transit method in the transitlist attribute   
        for t in self.transitlist: #turns transit method into minutes of transit. Driving takes 20 minutes and walking takes 10. In a more advanced app, this could be dynamic
            if t=='d': #d is for 'drive' here, not a default value
                drive=20 #driving takes 20 minutes
                self.transitlistm.append(drive) #records time in the transitlistm attribute
            else: 
                walk=10 #walking takes 10 minutes
                self.transitlistm.append(walk) #records time in the transitlistm attribtue
        
    def buffer(self, type=0): #method for accounting for buffer time
        while type!='m' and type!='p': #while clause ensures rawinput is repeated if a mistake is typed in. User will choose from two choices, m or p
            try: 
                type=raw_input("For a buffer of x minutes type m. For a buffer of x percent of your travel time, type p: ") #user chooses m (for minutes) or p (for percentage)
                if not (type=='m' or type=='p'):
                    raise ValueError #raise value error if not m or p 
            except ValueError:
                print "Invalid type of buffer. Please type m or p." #message telling user to type either m or p
        if type=='m': #logic if the user chooses to type in number of buffer minutes
            for i in self.schedule: #for loop for getting buffer for each appointment
        	buffers='d' #default value so that the while loop is started 
        	while isinstance(buffers, float)==False: #while loop ensures rawinput is repeated if a mistake is typed in. 
        	    try:
        	        buffers=float(raw_input("Do you need buffer for your {0} appointment? Type number of minutes: ".format(i)))
        	    except ValueError:
        	        print "Invalid buffer. Please enter a number" #error message if a number isn't typed in
        	    else:
        	        self.bufferlist.append(buffers) #records the buffertime in the bufferlist attribute   
        else: #logic if the user chooses to type in percentage of buffer time (as a % of travel time). The first while clause in buffer() ensures this will be 'p' since it's not 'm'  
            for i in self.schedule: 
        	buffers='d' #default value to get while loop started
        	while isinstance(buffers, float)==False: #while loop ensures rawinput is repeated if a mistake is typed in. 
        	    try:
        	        buffers=float(raw_input("Do you need buffer for your {0} appointment? Type percentage as a number: ".format(i)))
        	    except ValueError:
        	        print "Invalid buffer. Please enter a number"
        	    else:
        	        self.bufferlistp.append(buffers) #records the buffertime percentage in the bufferlistp attribute   
            for b, t in zip(self.bufferlistp, self.transitlistm): #forloop convers buffer percentage to time in minutes, zip command combines list arguments
                percentage=b*t/100
                self.bufferlist.append(percentage) #records buffer time in the bufferlist attribute

        
    def prep(self): #method for accounting for prep time
        for i in self.schedule: #for loop for getting prep time for each appointment
        	preps=0 #default value so that the for loop is started 
        	while isinstance(preps, float)==False: #while loop for ensuring rawinput prompts 
        	    try:
        	        preps=float(raw_input("How much preptime do you need for your {0} appointment? Type number of minutes: ".format(i)))
        	    except ValueError:
        	        print "Invalid preptime. Please enter a number"
        	    else:
        	        self.preplist.append(preps) #records the preptime in the preplist attribute       
    
    def result(self): #method for getting final result
        for s, t, b, p  in zip(self.schedule, self.transitlistm, self.bufferlist, self.preplist): #gets arguments from all lists
            time= s - datetime.timedelta(minutes=t+b+p) #gets result as a datetime.datetime object
            conversion=datetime.datetime.strftime(time, "%I:%M%p") #converts result into a nice looking string
            self.resultlist.append(conversion) #stores results in the resultlistattribute  
    
def main(): #main function that will run from this script
    schedule=[]
    items='d' #default value for whileloop
    while isinstance(items, int)==False: #ensures rawinput repeats if a mistake is typed in 
        try:
            items=int(raw_input("How many items on your schedule today?: "))
        except ValueError:
            print "Invalid entry. Please enter an integer"
    i=0
    while i < items: #while loop prompts you to input the times of things on your schedule
        sched=raw_input("Input the time of your appointments, in order, using the format of 11:00am or 2:00pm: ")
        #is there a good way to raise an error if the format isn't correct, or is that too hard here?
        schedule.append(sched) #adds times to the list schedule 	
        i = i + 1 #step function 
    schedule=Bounce(schedule)  #creates an instance of the main class
    print "Your schedule is {0}".format(schedule.schedule) #prints the schedule you typed in so you can see 
    schedule.transit() #runs the transit method
    schedule.buffer() #runs the buffer method (requires transit method has been run)
    schedule.prep() #runs the prep method 
    schedule.time() #runs the time method. Could have been done earlier, but works here too
    schedule.result() #runs the result method.
    print "The times you need to start getting ready are {0}".format(schedule.resultlist) #prints the results
  
if __name__ == '__main__': 
    main()
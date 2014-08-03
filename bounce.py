from datetime import datetime
#import pdb

class Bounce:
    """The Never-be-late prototype"""
  
    def __init__(self, schedule, transitlist=[]):
        self.schedule=schedule #starts with a daily schedule
        self.transitlist=transitlist #default empty list of transit methods
    
    def time(self):
        schedule=self.schedule
        schedule[:] = [datetime.strptime(x, '%I:%M%p') for x in schedule]
        self.schedule=schedule
    
    def transit(self): #method for accounting for transit time
        transitlist=self.transitlist
        for i in self.schedule:
        	transits=0
        	while transits!='d' and transits!='w':
        	    try:
        	        transits=raw_input("How will you be getting to your {0} appointment? Type d for drive and w for walk: ".format(i))
        	        if not (transits=='d' or transits=='w'):
        	            raise ValueError
        	    except ValueError:
        	        print "Invalid transit method. Please type d or w"
        	    else:
        	        self.transitlist.append(transits)
            
        self.transitlist=transitlist



if __name__ == '__main__':
    #pdb.set_trace()
    schedule=Bounce(['8:00pm', '5:00pm', '3:00pm'])
    schedule.transit()
    print schedule.schedule
    print schedule.transitlist
    print schedule.time()
    print schedule.schedule
    
#from datetime import date, datetime, time, timedelta

#a=05
#b=30

#schedule[:] = [datetime.strftime(x, '%I:%M%p') for x in schedule]


#dt = datetime.combine(date.today(), time(a, b)) + timedelta(minutes=10)
#print dt.time()
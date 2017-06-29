data_store = {
    "trips":0
    }

class trip_object(object):
    
    def __init__(self, launch, on, starttime, ontime, startmiles,
                 onmiles, leavetime, home, hometime, homemiles, work):
        self.launch = launch
        self.on = on
        self.starttime = starttime
        self.ontime = ontime
        self.startmiles = startmiles
        self.onmiles = onmiles
        self.leavetime = leavetime
        self.home = home
        self.hometime = hometime
        self.homemiles = homemiles
        self.work = work
        
    def time_calc(self, hours1, minutes1, hours2, minutes2):
        total_h = hours2 - hours1
        total_m = minutes2 - minutes1
    
        if total_m < 0:
            total_h -= 1
            total_m = 60 - abs(total_m)

        trip_time = str(total_h) + " hours " +  str(total_m) + " minutes"
        return trip_time
        
    def calculate(self):
        trip_a = int(self.onmiles) - int(self.startmiles)
        trip_b = int(self.homemiles) - int(self.onmiles)
        totalmiles = int(trip_a) + int(trip_b)
            
        th1 = int(self.starttime[0:2])
        tm1 = int(self.starttime[3:5])
        th2 = int(self.ontime[0:2])
        tm2 = int(self.ontime[3:5])

        th3 = int(self.leavetime[0:2])
        tm3 = int(self.leavetime[3:5])
        th4 = int(self.hometime[0:2])
        tm4 = int(self.hometime[3:5])

        point_AB = self.time_calc(th1, tm1, th2, tm2)
        point_BC = self.time_calc(th3, tm3, th4, tm4)
        time_on = self.time_calc(th2, tm2, th3, tm3)    
        allthedata = (trip_a, trip_b, time_on, totalmiles, point_AB, point_BC)
        return allthedata

    
 def make_trip(trip_number):
    if trip_number == 1:
        print ('You will now begin inputting trip data.\n'
               'For mileages, do not use commas. CORRECT: 90123 INCORRECT: 90,123\n'
               'For times, use 4 digit 24 hour time, CORRECT: 09:24 INCORRECT: 9:24\n'
               'If you do not follow these formats correctly, the program will error out\n')
    else:
        pass
        
    launch = input('\ninput launch point \n')
    startmiles = input('input your starting mileage \n')
    starttime = input('input your starting time \n')
    on = input('input your destinantion point \n')
    ontime = input('input your arrival time \n')
    onmiles = input('input your mileage upon arrival \n')
    leavetime = input('input your departure time \n')
    home = input("Where did you go next?")
    homemiles = input('input your home miles \n')
    hometime = input('input your home time \n') 
    workperformed = input('Decribe the work performed onsite \n')
    
    trip = trip_object(launch, on, starttime, ontime, startmiles,
                 onmiles, leavetime, home, hometime, homemiles, work)                 
    
    data_store["trip{0}".format (str(trip_number))] = trip.calculate
    data_store["trips"] += 1 
    
    print "Do you have another trip to add?\n"
    again = raw_input ("y/n?\n").lower()
    if again == "y":
        make_trip(trip_number + 1)
    else:
        pass
        
def rsheet():
    print ("Do you have anything to add to the routersheet?")
    answer = input("y/n? ").lower()
    if answer == "y": 
        info = input("Enter your routersheet info \n")
        rsheet = ("ADD TO ROUTERSHEET: \n" + info)
        data_store["rsheet"] = rsheet
    else:
        pass

#this next function looks querys the user for any info that needs to be added to the contacts sheet
def csheet():
    print ("Do you have anything to add to the contacts sheet? ")
    answer = input("y/n? ").lower()
    if answer == "y":
        info = input("Enter your contactsheet info \n")
        csheet = ("ADD TO CONTACTSHEET: \n" + info)
        data_store["csheet"] = csheet
    else:
        pass
   
def nsheet():
    print ("Are there any additional notes you would like to add? ")
    answer = input("y/n? ").lower()
    if answer == "y":
        info = input("Add your notes now \n")
        notes = ("Additional notes: \n" + info)
        data_store["nsheet"] = nsheet
    else:
        pass
#PICK UP HERE
def generate(data):
    grand_total = 0
    for i in range(1, data["trips"] + 1):
        trip = "trip" + str(i)    
        
def main():
    make_trip(1)
    rsheet()
    csheet()
    nsheet()
    generate(data_store)
    
    
##"shop", "etim", "09:00", "09:30", "90000", "90018", "10:00", "shop", "10:30", "90036", "Did stuff"
        

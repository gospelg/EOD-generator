##EOD creator version 1

## sheet1 will query the user for any changes that should be made to the router sheet

def sheet1():
    print ("Do you have anything to add to the routersheet?")
    answer = input("y/n? ").lower()
    
    if answer == "y": 
        global rsheet
        rsheet = input("Enter your routersheet info")
        sheet2()
    
    else:
        sheet2()

#this next function looks querys the user for any info that needs to be added to the contacts sheet
def sheet2():
    print ("Do you have anything to add to the contacts sheet? ")
    answer = input("y/n? ").lower()
    
    if answer == "y":
        global csheet
        csheet = input("Enter your contactsheet info ")
        notesheet()

    else:
        notesheet()

def notesheet():
    print ("Are there any additional notes you would like to add?")
    answer = input("y/n? ").lower()
    
    if answer == "y":
        global notes
        notes = input("Add your notes now /n")
        generate()
    else:
        generate()


##perform ze mathzz
##this first one will calculate trip times

def time_calc(hours1, minutes1, hours2, minutes2):
    total_h = hours2 - hours1
    total_m = minutes2 - minutes1
    
    if total_m < 0:
        total_h -= 1
        total_m = 60 - abs(total_m)

    trip_time = str(total_h) + " hours " +  str(total_m) + " minutes"
    return trip_time
#this function does most of the calculating, including distances and calls the time_calc function to find elapsed times.
def mathisfun():
    
    trip_a = int(onmiles) - int(startmiles)
    trip_b = int(homemiles) - int(onmiles)
    totalmiles = int(trip_a) + int(trip_b)
  
#this takes user string inputs and converts them to formatting freindly to the time_calc
  
    th1 = int(starttime[0:2])
    tm1 = int(starttime[3:5])
    th2 = int(ontime[0:2])
    tm2 = int(ontime[3:5])

    th3 = int(offtime[0:2])
    tm3 = int(offtime[3:5])
    th4 = int(hometime[0:2])
    tm4 = int(hometime[3:5])
    

    global point_AB
    point_AB = time_calc(th1, tm1, th2, tm2)

    global point_BC
    point_BC = time_calc(th3, tm3, th4, tm4)
   
    global time_on
    time_on = time_calc(th2, tm2, th3, tm3)    

    global allthedata 
    allthedata = (trip_a, trip_b, time_on, totalmiles)
    

##this is the final function, which prints everything to human freindly output
  
def generate():
  
    mathisfun()

    
    with open("eod.txt", "w") as text_file:
        print("Starting miles: {0} \nEnding miles: {1} \nTOTAL: {2} \n".format(startmiles, homemiles, allthedata[3]), file=text_file)
        print("From {0} to {1}: {2} - {3} ({4} miles) {5} - {6} ({7}) <-travel".format(launch, destination, startmiles, onmiles, allthedata[0], starttime, ontime, point_AB), file=text_file)
        print("From {0} to {1} ({2}) <- onsite. \n\n{3}\n".format(ontime, offtime, time_on, workperformed), file=text_file)
        print("From {0} to {1}: {2} - {3} ({4} miles) {5} - {6} ({7}) <- travel.".format(destination, launch, onmiles, homemiles, allthedata[1], offtime, hometime, point_BC), file=text_file)    



##gather user inputs
#this should be a function, but I have not figured out how to make this thing work without these as global var. so i have inactivated the function, which I will activate later
#def data_grab():
  
#    launch = input('input launch point \n')
#   startmiles = input('input your starting mileage \n')
#    starttime = input('input your starting time \n')
#    destination = input('input your destinantion point \n')
#    ontime = input('input your arrival time \n')
#    onmiles = input('input your mileage upon arrival \n')
#    offtime = input('input your departure time \n')
#    homemiles = input('input your home miles \n')
#    hometime = input('input your home time \n') 
#    workperformed = input('Decribe the work performed onsite \n')

#    sheet1()

#def main():
#    data_grab()
#this serves as the main operation of the program. This first gathers input from the user, then calls the sheet1 function, which calls
#sheet2, which calls sheet3, which calls generate, which is the actual output. So from here, it starts a chain of functions that
#form the meat of the program. It is my intention to turn this section into a seperate function, and probably use classes to eliminate
#all the global vars. I also want to add error checking to ensure input is in the right format.

launch = input('input launch point \n')
startmiles = input('input your starting mileage \n')
starttime = input('input your starting time \n')
destination = input('input your destinantion point \n')
ontime = input('input your arrival time \n')
onmiles = input('input your mileage upon arrival \n')
offtime = input('input your departure time \n')
homemiles = input('input your home miles \n')
hometime = input('input your home time \n') 
workperformed = input('Decribe the work performed onsite \n')

sheet1()



#this is a set of predefined variables to be used for testing porpuses
#starttime = "13:00" 
#ontime = "13:20"
#offtime = "13:40"
#hometime = "14:00"
#startmiles = "100"
#onmiles = "110"
#homemiles = "120"
#launch = "shop"
#destination = "dog"
#workperformed = "yaddy yaddy yadda"

    

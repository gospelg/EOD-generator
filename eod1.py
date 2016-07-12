##EOD creator version 1

import math

## define functions 
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
        mathisfun()
    else:
        mathisfun()


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

def mathisfun():
    
    trip_a = int(onmiles) - int(startmiles)
    trip_b = int(homemiles) - int(onmiles)
    totalmiles = int(trip_a) + int(trip_b)
    
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

#will tally up and print some totals

#def totals():
#    print ("Starting miles: " + startmiles)
#    print ("Ending miles: " + homemiles)
#    print ("TOTAL: " + str(allthedata[3])



##this is the final function, which prints everything to human freindly output
  
def generate():
  
    mathisfun()

    
    print ("Starting miles: " + startmiles)
    print ("Ending miles: " + homemiles)
    print ("TOTAL: " + str(allthedata[3]) + "\n")
    print ("From " + launch + " to " + destination + ': ' + startmiles + " - "
+ onmiles + " (" + str(allthedata[0]) + " miles) " + starttime + " - " + ontime +
" (" + point_AB + ")" + "<- travel." + "From " + ontime + "- " + offtime + " (" + str(allthedata[2]) + ") <- onsite.")
    print ("\n" + workperformed + "\n")
    print ("From " + destination + " to " + launch + ': ' + onmiles + " - "
+ homemiles + " (" + str(allthedata[1]) + " miles) " + offtime + " - " + hometime +
" (" + point_BC + ")" + "<- travel.")

    

     




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
generate()


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
